import flask
from flask import request
import json



app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/test', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/send_voice', methods = ['POST'])
def send_voice():
    data = request.form # a multidict containing POST data

    x = "What did you say to me you little shit!? THIS? " + data.get("myField")
    return x

app.run()