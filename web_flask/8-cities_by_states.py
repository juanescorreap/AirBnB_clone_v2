#!/usr/bin/python3
"""
 script that starts a Flask web application
"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def display_states():
    return render_template('8-cities_by_states.html',
                           display=storage.all(State).values())


@app.teardown_appcontext
def close_alchemy(self):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')