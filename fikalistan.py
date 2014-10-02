from flask import Flask, url_for, g, render_template, request, flash, redirect
import database
from database import query_db, commit_db

app = Flask(__name__)
app.config.from_object(database)

@app.before_request
def before_request():
    g.db = database.connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def groups():
    entries = query_db(g, 'select group_name from groups order by group_name desc', list=True)
    return render_template('groups.html', entries=entries)

@app.route('/add_group', methods=['POST'])
def add_entry():
    commit_db(g, 'insert into groups (group_name) values (?)',
                 [request.form['group']])
    flash('New entry was successfully posted')
    return redirect(url_for('groups'))

@app.route('/<group>')
def participants(group):
    groupID = query_db(g, 'select id from groups where group_name = ?', [group], one=True)
    return group + " has ID " + str(groupID[0])


if __name__ == '__main__':
    app.debug = True
    app.run()
