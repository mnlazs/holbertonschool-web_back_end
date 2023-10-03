#!/usr/bin/env python3
"""Flask Task
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_word():
  """template"""
  return 

if __name__ == "__main__":
    app.run()
