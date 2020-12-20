import os

from flask import (
    Flask, render_template, flash, redirect, 
    session, request, url_for)
from flask_pymongo import PyMongo 
from bson.objectid import ObjectId  
from werkzeug.security import generate_password_hash, check_password_hash   
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_tasks")
def index():
    collections = mongo.db.tasks.find()
    return render_template("task.html", collect=collections)


@app.route("/register", methods=["GET", "POST"])
def regist():
    if request.method == "POST":
        username = request.form.get("username").lower()
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": username})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for('regist'))

        if password == confirm:
            register = {"username": username,
                        "password": generate_password_hash(
                            password)
                            } 
            mongo.db.users.insert_one(register)  
            
        # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful!")

        else:
            flash("Passwords do not match.")

    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
