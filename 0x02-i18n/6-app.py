#!/usr/bin/env python3
""" flask run module """
from flask import Flask, request, render_template, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """ Get locale from request """
    locale = request.args.get('locale')
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user.get('locale') in app.config["LANGUAGES"]:
        return g.user.get('locale')
    header_locale = request.headers.get('locale')
    if header_locale and header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user(login_as):
    """Retrieve user information based on the provided login ID."""
    if not login_as or not users.get(int(login_as)):
        return None
    return users.get(int(login_as))


@app.before_request
def before_request():
    """Set the user information as a global variable
    before processing each request."""
    g.user = get_user(request.args.get('login_as'))


@app.route("/")
def home():
    """Renders a basic html template"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run()
