from flask import Flask, url_for, g, render_template, request, flash, redirect
import config

app = Flask(__name__)
app.config.from_object(config)

@app.before_request
def before_request():
    g.db = config.connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    cur = g.db.execute('select group_name from groups order by group_name desc')
    entries = [row[0] for row in cur.fetchall()]
    return render_template('groups.html', entries=entries)

@app.route('/add_group', methods=['POST'])
def add_entry():
    g.db.execute('insert into groups (group_name) values (?)',
                 [request.form['group']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('index'))

@app.route('/<group>')
def participants(group): return group + " not yet implemented"


if __name__ == '__main__':
    app.debug = True
    app.run()
