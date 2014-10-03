from flask import Flask
from .model import db
from .views import fikalistan

app = Flask(__name__) #create our application object
app.config.from_object('config.Configuration') #load our local config file

db.init_app(app)

app.register_blueprint(fikalistan)