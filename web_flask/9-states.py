#!/usr/bin/python3
"""
 script that starts a Flask web application
"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.routes('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_and_city(id=None):
    """Fetches data from the storage engine"""
    states_list = storage.all(State)
    if id:
        key = "State." + id
        if key in states_list:
            state = states_list[key]
        else:
            state = None
    else:
        state = storage.all(State).values()
    return render_template('9-states.html', states=state, id=id)


@app.teardown_appcontext
def close_alchemy(self):
    """Closes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
