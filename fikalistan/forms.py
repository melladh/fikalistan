from wtforms import fields
from flask.ext.wtf import Form

class GroupForm(Form):
    name = fields.StringField()

class ParticipantForm(Form):
    name = fields.StringField()
    group_id = fields.HiddenField()