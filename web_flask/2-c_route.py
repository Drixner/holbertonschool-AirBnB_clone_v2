#!/usr/bin/python3
"""Script to start flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Return messages"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_HBNB():
    """Return messages"""
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def varible_text(text):
    """Return messages"""
    new_text = text.replace('_', ' ')
    return ('C {:s}'.format(escape(new_text)))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
