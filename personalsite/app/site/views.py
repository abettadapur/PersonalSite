#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template

from . import site_blueprint


@site_blueprint.route('/')
def index():
    return render_template('site/index.html')