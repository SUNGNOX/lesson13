# -*- coding: utf-8 -*-
from flask import Flask
from werkzeug.routing import BaseConverter
#from flask.ext.bootstrap import Bootstrap
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from flask_sqlalchemy import SQLAlchemy
from os import path
from .views import create_view

basedir = path.abspath(path.dirname('__file__'))
nav = Nav()
bootstrap = Bootstrap()
db = SQLAlchemy()

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex=items[0]#regex的属性名不能改动

def create_app():
    app = Flask(__name__)
    app.url_map.converters['regex'] = RegexConverter
    app.config.from_pyfile('config')
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    nav.register_element('top', Navbar(u'导航栏',
                                       View(u'主页', 'index'),
                                       View(u'服务', 'serve'),
                                       View(u'关于', 'about'),
                                       View(u'内容', 'context'),
                                       View(u'登录', 'login')
                                       ))
    nav.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    create_view(app)
    return app
