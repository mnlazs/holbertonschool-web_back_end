#!/usr/bin/env python3
""" Task 3 """
from flask_babel import Babel
from flask import Flask, render_template, request

app = Flask(__name__)
babel = Babel(app)


class Config:
    """descripcion de la clase"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Configurar la aplicación Flask con la clase de configuración
app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index():
    """template rendering"""
    return render_template('3-index.html')


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


if __name__ == '__main__':
    app.run()
