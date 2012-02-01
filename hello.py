#!/usr/bin/env python

from flask import Flask
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/time")
def time_limit():
	deadline = datetime(2012,2,5,17)
	delta = deadline - datetime.now()
	hours = (delta.days * 24) + (delta.seconds / 60 / 60)
	s = str(hours) + " hours left. Hurry up!"
	return s

if __name__ == "__main__":
    app.run()
