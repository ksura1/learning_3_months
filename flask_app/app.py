from flask import Flask, request, render_template
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
@app.route("/get_input")
def input():
    i = request.args.get('input')
    return f"<p> input: {i}</p>"
# api2: file_name in argument
"""
? file_name=requirment.txt

read file , display content file on page
"""
@app.route("/get_file")
def file():
    f = request.args.get('file_name')
    log = open(f, 'r').read()
    return log

# api3 : use template in flask
"""
display story or wikipedia page link
"""
@app.route("/")
def index():
    return render_template('index.html')

print('Test')

#api4
@app.route("/user", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Print the form data to the console
        for key, value in request.form.items():
            print(f'{key}: {value}')
    return render_template('user_input.html')

if __name__ == "__main__":
    app.run(debug=True)