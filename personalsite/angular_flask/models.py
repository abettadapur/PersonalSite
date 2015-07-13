from datetime import datetime

from angular_flask.core import db
from angular_flask import app

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Project %r>' % self.title

class WorkExperience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    current = db.Column(db.Boolean)
    location = db.Column(db.String(80))
    description = db.Column(db.String(80))

    def __repr__(self):
        return '<WorkExperience %r>' % self.title


class WorkItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer)
    #work_experience_id = db.Column(db.Integer, db.ForeignKey("workexperience.id"))
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<WorkItem %d>' % self.order


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    value = db.Column(db.Integer)

    def __repr__(self):
        return '<Skill %r>' % self.title


# models for which we want to create API endpoints
app.config['API_MODELS'] = {
    'project': Project, 
    'work_experience': WorkExperience, 
    'skill': Skill,
}

# models for which we want to create CRUD-style URL endpoints,
# and pass the routing onto our AngularJS application
app.config['CRUD_URL_MODELS'] = {
    'project': Project,
    'work_experience': WorkExperience, 
    'skill': Skill
}
