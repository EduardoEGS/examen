from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def index_():
    return render_template('login.html')

@app.route("/login.html")
def index():
    return render_template('login.html')