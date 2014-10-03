from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()

class Group(db.Model):
    __tablename__ = 'group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    participants = db.relationship('Participant', backref=backref('group'), lazy='select')

    def __repr__(self):
        return '<Group {:d} {}>'.format(self.id, self.name)

    def __str__(self):
        return self.name


class Participant(db.Model):
    __tablename__ = 'participants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))

    def __repr__(self):
        r = '<Participant {:d} in group with ID {}: {}>'
        return r.format(self.id, self.group_id, self.name)

    def __str__(self):
        return self.name


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))
    date = db.Column(db.Date)

    def __repr__(self):
        return '<Event for participant {:d} at date {}>'.format(self.participant_id, self.date)