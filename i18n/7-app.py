#!/usr/bin/env python3
""" Task 5"""
from flask_babel import Babel
from flask import Flask, render_template, request, g
import pytz

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.timezoneselector
def get_timezone():
    """determina la mejor zona horaria para la app"""
    if request.args.get('timezone'):
        timezone = request.args.get('timezone')
        try:
            return timezone(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    elif g.user and g.user.get('timezone'):
        try:
            return timezone(g.user.get('timezone')).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


class Config:
    """ cconfiguracion del lenguaje"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index():
    """ first index template to getting started translate
    Args:
        template rendering
    """
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """ funcion preferencia del Idioma
    """
    # obtiene la preferencia de idioma del usuario
    locale = request.args.get('locale')
    # si se especifica un idioma en la URL y es compatible
    if locale and locale in Config.LANGUAGES:
        return locale
    # si el usuario esta autenticado, lo devuelve
    if hasattr(g, "user") and g.user["locale"] in Config.LANGUAGES:
        return g.user["locale"]
    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user():
    """ Get user from mock db "users"
    Returns:
        [type]: [description]
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))


@app.before_request
def before_request():
    """ logged in user if is paased like args
    """
    user = get_user()
    if user:
        g.user = user


if __name__ == '__main__':
    app.run('0.0.0.0', '5000')