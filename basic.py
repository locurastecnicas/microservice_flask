from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return("Hello World!")
@app.route("/login")
def login():
    return("Login page!!!")
@app.route("/admin")
def admin():
    return("Admin page!!!!")
