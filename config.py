import sqlite3
from flask import Flask
from contextlib import closing

# configuration
DATABASE = '/tmp/fikalistan.db'
DEBUG = True
SECRET_KEY = 'hej'
USERNAME = 'root'
PASSWORD = ''

def connect_db():
    return sqlite3.connect(DATABASE)

def init_db():
    app = Flask(__name__)
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

if __name__ == '__main__':
    selection = raw_input("Warning! This will reset any previously created database entries! Continue? Y/n   ")
    if selection == "Y":
        init_db()
        print "Created database"
    else:
        print "Exiting"