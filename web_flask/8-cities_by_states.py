#!/usr/bin/python3
"""
 script that starts a Flask web application
"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def display_cities():
    """ Fetches data from the storage engine"""
    return render_template('8-cities_by_states.html',
                           display=storage.all(State).values())


@app.teardown_appcontext
def close_alchemy(self):
    """Closes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
