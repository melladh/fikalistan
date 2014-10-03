from flask import render_template, Blueprint, flash, url_for, redirect
from markupsafe import Markup
from fikalistan.model import Group, Participant, db

from .forms import GroupForm, ParticipantForm

fikalistan = Blueprint("fikalistan", __name__)

@fikalistan.route('/')
def groups():
    group_form = GroupForm()
    groups = db.session.query(Group).all()
    results = [group.name for group in groups]
    return render_template('groups.html', form=group_form, data=results)

@fikalistan.route('/add_group', methods=['POST'])
def add_group():
    form = GroupForm()
    group = Group()
    form.populate_obj(group)
    db.session.add(group)
    db.session.commit()
    flash("Newly created group")
    return redirect(url_for('.participants', group=group.name))

@fikalistan.route('/<group>')
def participants(group):
    group_obj = db.session.query(Group).filter_by(name=group).first()    # name is unique
    if group_obj is None:
        return render_template('404.html', message= "No group " + group)
    participant_form = ParticipantForm()
    participant_form.group_id.data = group_obj.id  #hide a group reference for the post
    participants_list = group_obj.participants
    return render_template('participants.html', form=participant_form, group=group_obj.name,
                           participants=participants_list)


@fikalistan.route('/add_participant', methods=['POST'])
def add_participant():
    form = ParticipantForm()
    group_obj = db.session.query(Group).filter_by(id=form.group_id.data).first()
    if group_obj is None:
        return render_template('404.html', message= "No group with ID " + form.group_id.data)
    participant = Participant()
    form.populate_obj(participant)
    db.session.add(participant)
    db.session.commit()
    return redirect(url_for('.participants', group=group_obj.name))

def _make_link(group):
    url = url_for(".participants", group=group)
    return Markup('<h2><a href="{url}">{name}</a></h2>').format(url=url, name=group)
