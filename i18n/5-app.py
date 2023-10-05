#!/usr/bin/env python3
"""Mocking"""

from flask import Flask, g, request, render_template
from flask_babel import Babel
from os import getenv
from typing import Union

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


class Config:
    """estableciendo la clase Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index():
    """ first index template to getting started translate"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """ definicion de la clase
    """
    locale = request.args.get('locale')
    if locale is None:
        lang = Config.LANGUAGES
        return request.accept_languages.best_match(lang)
    else:
        return locale


@app.before_request
def before_request():
    user_id = request.args.get("login_as")
    g.user = get_user(int(user_id)) if user_id else None


def get_user(user_id, login_as):
    usuario = users.get(user_id)
    if usuario and login_as:
        return usuario
    return None


if __name__ == '__main__':
    app.run("0.0.0.0', '5000")
