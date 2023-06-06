from flask import Flask
import datetime

# flask run --reload
 
app = Flask(__name__)

@app.route("/test")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/get_todays_date")
def todays_date():
    today = datetime.datetime.now()
    return f"<p> today date : {today}</p>"

# api1 : taking input from argument: display in page
"""
?input=text

text will be on webpage
"""

# api2: file_name in argument
"""
? file_name=requirment.txt

read file , display content file on page
"""

# api3 : use template in flask
"""
display story or wikipedia page link
"""






