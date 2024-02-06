#!/usr/bin/env python3
""" flask run module """
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def home():
    """Renders a basic html templat"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
