#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint

site_blueprint = Blueprint('site', __name__)

from . import views