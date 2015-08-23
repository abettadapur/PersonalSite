from angular_flask import app, admin

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy(app)

api_manager = APIManager(app, flask_sqlalchemy_db=db)

from angular_flask.models import Project, WorkExperience, WorkItem, Skill

api_manager.create_api(Project, methods=['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(WorkExperience, methods=['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(WorkItem, methods=['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(Skill, methods=['GET', 'POST', 'DELETE', 'PUT'])

admin.add_view(ModelView(Project, db.session))
admin.add_view(ModelView(WorkExperience, db.session))
admin.add_view(ModelView(WorkItem, db.session))
admin.add_view(ModelView(Skill, db.session))
