#!/usr/bin/env python3
"Task 1 - Babel Set up"
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__) #creando la instancia de la app Flask
babel = Babel(app) #configurando la instacia babel


class Config: #creando la clase con los idiomas disponibles
  """descripcion de la clase"""
  LANGUAGES = ["en", "fr"]
  BABEL_DEFAULT_LOCALE = "en"
  BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config) #Configurar la aplicación Flask con la clase de configuración

@app.route("/")
def index():
    """template"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
