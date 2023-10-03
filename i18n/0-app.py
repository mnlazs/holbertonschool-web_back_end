#!/usr/bin/env python3
"""Flask Task
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  """template"""
  return 

if __name__ == "__main__":
    app.run()
