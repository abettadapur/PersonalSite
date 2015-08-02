import os
import json
from flask import Flask, request, Response
from flask import render_template, send_from_directory, url_for
from flask_admin import Admin

app = Flask(__name__)

admin = Admin(app, name='personalsite', template_mode='bootstrap3')

app.config.from_object('angular_flask.settings')

app.url_map.strict_slashes = False

import angular_flask.core
import angular_flask.models
import angular_flask.controllers
