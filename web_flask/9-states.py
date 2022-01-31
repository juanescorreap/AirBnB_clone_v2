#!/usr/bin/python3
"""
 script that starts a Flask web application
"""
from models import storage
from flask import Flask, render_template
from models.state import State
import os
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_and_city(id=None):
    """Fetches data from the storage engine"""
    states = storage.all(State)
    if id:
        key = 'State.{}'.format(id)
        if key in states:
            states = states[key]
        else:
            states = None
    else:
        states = storage.all(State).values()
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def close_alchemy(self):
    """Closes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
