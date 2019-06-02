

from flask import Flask, current_app,request,Request



app = Flask(__name__)


#AppContext
#RequestContext

with app.app_context():
    a = current_app

    d = current_app.config['DEBUG']
