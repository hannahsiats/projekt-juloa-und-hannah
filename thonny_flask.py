from flask import Flask
app = Flask(__name__)
@app.route("/")
def main_page():
    return "Meine Hauptseite"

@app.route("/hello/<string:username>")
def greet_user(username):
    return username
