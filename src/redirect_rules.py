
import re
import json
import requests as rq
import datetime as dt

from .conf.general_conf import REDIRECT_SOURCES
from .logging import logger
from .util import Util


class RedirectRules:
    """
    """

    def __init__(self):
        """
        """
        logger.info('init RedirectRules')
        self.redirect_rules = []
        self.start_datetime = Util.get_time()
        self.update()

    def update(self):
        """
        """
        logger.info('start RedirectRules.update()')
        li_rule = []

        for url in REDIRECT_SOURCES:
            logger.debug(f'url={url}')
            r = rq.get(url)
            try:
                data = r.content.decode('utf-8')
                li = json.loads(data)
                for e in li:
                    e['source'] = url
                li_rule += li
            except:
                logger.error('message:', exc_info=True)

        logger.debug('redirect rules:')
        logger.debug(li_rule)

        self.redirect_rules = li_rule

    def get_url(self, path):
        """
        """
        for e in self.redirect_rules:
            regex = e['regex']
            route = e['route']
            if re.compile(regex).match(path):
                s = re.sub(regex, route, path)
                logger.info(f'route={s}')
                return s

        logger.info(f'route=info')
        return '/info'


rules = RedirectRules()
