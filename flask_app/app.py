from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/test")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/get_todays_date")
def todays_date():
    today = datetime.datetime.now()
    return f"<p> today date : {today}</p>"