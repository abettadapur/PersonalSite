#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)


def create_app():
    from site import site_blueprint
    app.register_blueprint(site_blueprint)
    return app