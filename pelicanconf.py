#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'hyunmin'
SITENAME = '물개발자'
SITEURL = 'https://harry81.github.io'

PATH = 'content'
TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'en'

GITHUB_URL = 'http://github.com/harry81/'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = "feeds/tag_%s.atom.xml"


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Github', 'https://github.com/harry81'),)

DEFAULT_PAGINATION = 5
STATIC_PATHS = ['images', 'pdfs']

THEME = "/home/harry/pelican-themes/tuxlite_zf/"

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets', 'sitemap', 'gravatar', 'i18n_subsites']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
