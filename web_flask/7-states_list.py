#!/usr/bin/python3
'''a script that starts a Flask web application'''

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list():
     '''/states_list: display a HTML page: (inside the tag BODY)'''
     states = storage.all("State").values()
     return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown():
     '''After each request you must remove the current SQLAlchemy Session'''
     storage.close()

if __name__ == "__main__":
     app.run(host='0.0.0.0', port='5000')