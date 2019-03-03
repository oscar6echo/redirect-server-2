
import json
import atexit
import logging

from flask import Flask, redirect, send_from_directory

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from .conf.general_conf import REFRESH_SECONDS, LOGGER_NAME
from .redirect_rules import RedirectRules
from .util import Util


logger = logging.getLogger(LOGGER_NAME)
vue_dist = Util.get_dist()

app = Flask(__name__, static_folder=vue_dist)
app.config['DEBUG'] = True


@app.route('/static/<path:path>')
def send_static(path):
    """
    """
    logger.info(f'static path={path}')
    return send_from_directory(vue_dist, path)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def send_data(path):
    """
    """
    logger.info(f'data path={path}')

    if path == 'redirect-rules':
        data = {
            'updateTime': Util.get_time(),
            'redirectRules': rules.redirect_rules,
        }
        return json.dumps(data)

    if path == 'redirect-server-admin':
        data = {
            'startTime': rules.start_datetime,
            'updatePeriod': REFRESH_SECONDS,
        }
        return json.dumps(data)

    radical = 'test-shorturl-'
    if path.startswith(radical):
        path2 = path[len(radical):]
        data = {
            'testRedirectUrl': rules.get_url(path2)
        }
        return json.dumps(data)

    if path == 'info':
        return redirect('/static/index.html')

    url = rules.get_url(path)
    logger.info(f'redirect={url}')

    return redirect(url, code=301)


@app.after_request
def allow_cors(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


rules = RedirectRules()


scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    id='update-redirect-rules',
    func=rules.update,
    trigger=IntervalTrigger(seconds=REFRESH_SECONDS),
    replace_existing=True)

atexit.register(lambda: scheduler.shutdown())
