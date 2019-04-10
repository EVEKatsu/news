#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Administrator'
SITENAME = 'いぶかつ☆にゅーす'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

DEFAULT_DATE_FORMAT = '%Y年%m月%d日'

THEME = 'theme'

FAVICON = 'favicon.jpg'
FAVICON_TYPE = 'image/jpg'

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/' + FAVICON: { 'path': FAVICON },
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu
MENUITEMS = (
    ('Twitter', 'ic-twitter', 'https://twitter.com/evekatsu'),
    ('Archives', 'ic-posts', 'https://evekatsu.github.io/news/archives.html'),
    ('Ranking', 'ic-star', 'https://evekatsu.github.io/ranking/'),
    ('GitHub', 'ic-link', 'https://github.com/EVEKatsu'),
)

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/evekatsu'),
          ('feed', 'feeds/all.atom.xml'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
