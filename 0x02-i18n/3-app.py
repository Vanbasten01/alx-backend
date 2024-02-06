#!/usr/bin/env python3
""" flask run module """
from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Function to determine the preferred locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home():
    """Renders a basic html templat"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
