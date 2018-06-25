from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")
  
@app.route("/register")
def signup():
  return render_template("register.html")  
  
@app.route("/signin")
def signin():
  return render_template("signin.html")  

app.run()