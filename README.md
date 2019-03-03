# Redirect Server

## 1 - Overview

This repo contains a minimalist [Flask](http://flask.pocoo.org/docs/1.0/) redirect server.

The redirect rules are initally loaded from the source files listed in the `REDIRECT_SOURCES` in file [general_conf.py](https://github.com/oscar6echo/redirect-server-2/blob/master/src/conf/general_conf.py) and updated every `REFRESH_SECONDS` (defined in the same file) seconds.

Each redirect rule consists of:
+ A [regex](https://www.regular-expressions.info/) to match short urls
+ A route i.e. a corresponding [replacement string](https://www.regular-expressions.info/replacetutorial.html)
+ A source file from where the rule is read

Redirect rules are ordered by
+ source file - see examples [redirect-rules-1.json](https://github.com/oscar6echo/redirect-server-2/blob/master/sample/redirect-rules-1.json) and [redirect-rules-2.json](https://github.com/oscar6echo/redirect-server-2/blob/master/sample/redirect-rules-2.json)
+ then by order of entries in each source file

If the path of a requested url, i.e. the url exluding `http://host:port/`, matches a regex, its replacement string is the new destination url. The server then sends a redirect message with code = [HTTP 301 (Moved Permamently)](https://en.wikipedia.org/wiki/HTTP_301).


To test and learn about regex, see [regex101.com](https://regex101.com/).


## 2 - Install

### 2.1 - Python

If you have Python3 installed:

```bash
$ git clone https://github.com/oscar6echo/redirect-server
$ cd redirect-server
$ pip install -r requirements.txt
# flask werkzeug - debug only
$ python run-debug.py
# waitress - production
$ python run.py
# gunicorn - production
$ gunicorn --config server/conf/gunicorn_conf.py server:app
```

### 2.1 - Docker

If you have Docker installed:

-   Development mode - Hot reload server upon src/ folder change

```bash
# build image
$ docker build -t demo-api -f Dockerfile.dev .
# run container
$ docker run --rm -it -p 5000:5000 -v $(pwd)/src:/app/src demo-api bash
# from inside container launch src
root@id:/app# gunicorn --config src/conf/gunicorn_conf.py src:app
```

-   Production mode

```bash
# build image
$ docker build -t demo-api -f Dockerfile.prd .
# run container
$ docker run --rm -it -p 5000:5000 demo-api
```

## 3 - SSL certificates

If corporate SSL certificates need be installed add the following lines:

+ in the [requirements.txt](requirements.txt) file:

```bash
# example of proprietary package
certifi_sg
```

+ in the [__init__.py](__init__.py) file:

```python
from certifi_sg import add_sg_certificates

# appends SG certificates to certifi cacerts.pem file only if not there yet
add_sg_certificates()
```

## 4 - Dev


The frontend is a [Vue](https://vuejs.org) app built with [@vue/cli](https://cli.vuejs.org/).  
See their doc for more info.



