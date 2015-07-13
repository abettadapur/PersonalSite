from angular_flask import app

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

db = SQLAlchemy(app)

api_manager = APIManager(app, flask_sqlalchemy_db=db)

from angular_flask.models import Project, WorkExperience, WorkItem, Skill
api_manager.create_api(Project, methods=['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(WorkExperience, methods=['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(WorkItem, methods=['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(Skill, methods=['GET', 'POST', 'DELETE', 'PUT'])
