#!/usr/bin/env python3
"Task 1 - Babel Set up"
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)  # creando la instancia de la app Flask
babel = Babel(app)  # configurando la instacia babel


class Config:  # creando la clase con los idiomas disponibles
    """descripcion de la clase"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Configurar la aplicación Flask con la clase de configuración
app.config.from_object(Config)


@app.route("/")
def index():
    """template"""
    return render_template("0-index.html")


@babel.localeselector
def get_locale():
    """determinar el idioma que debe utilizarse"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run()
