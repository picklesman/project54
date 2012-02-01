from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/timelimit")
def time_limit():
    return 'Only 54 hours total!'

if __name__ == "__main__":
    app.run()
