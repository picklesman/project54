#!/usr/bin/env python

from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/title")
def title()
    return "Hate to Wait!"

@app.route("/time")
def time_limit():
	deadline = datetime(2012,2,5,17)
	delta = deadline - datetime.now()
	s = "%s days, %s hours left. <br> Hurry up! Don't forget to breathe." % (delta.days, delta.seconds/3600)
	return s

if __name__ == "__main__":
    app.run()
