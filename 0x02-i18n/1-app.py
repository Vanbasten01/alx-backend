#!/usr/bin/env python3
""" flask run module """
from flask import Flask
from flask_babel import Babel
from flask import render_template

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def home():
    """Renders a basic html templat"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
