import os
from flask_mail import Mail, Message
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

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.environ.get("nilssonstadtjanst@gmail.com")
app.config['MAIL_PASSWORD'] = s.environ.get('obtmimgynaxizidz')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_tasks")
def index():
    collections = list(mongo.db.tasks.find())
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
                            password)} 
            mongo.db.users.insert_one(register) 
            
        # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful!")
            return redirect(url_for('profile', username=session["user"]))
        else:
            flash("Passwords do not match.")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # CHECK IF USERNAME EXIST IN THE DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            #CHECKING IF HASHED PASSWORD MATCHES USERS INPUT   
            if check_password_hash(
                existing_user[
                    "password"], request.form.get("password")):
                session["user"] = request.form.get(
                    "username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(
                    url_for('profile', username=session["user"]))
            else:
                # IF PASSWORD DOESN'T MATCH
                flash("Invalid Password Match")
                return redirect(url_for('login'))

        else:
            # IF USERNAME DOESN'T EXIST
            flash("Incorrect Username and/or Password")
            return redirect(url_for('login')) 
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grapping the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)
    
    return render_template(url_for('login'))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        if "user" in session:
            is_urgent = "on" if request.form.get("is_urgent") else "off"
            task = {
                "category_name": request.form.get("category_name"),
                "description": request.form.get("description"),
                "date": request.form.get("date"),
                "address": request.form.get("address"),
                "email": request.form.get("email"),
                "phone_number": request.form.get("phone_number"), 
                "is_urgent": is_urgent,
                "created_by": session["user"]
            }
            mongo.db.tasks.insert_one(task)
            flash("Booking Successfully Added")
            return redirect(url_for("index"))
        else:
            is_urgent = "on" if request.form.get("is_urgent") else "off"
            task = {
                "category_name": request.form.get("category_name"),
                "description": request.form.get("description"),
                "date": request.form.get("date"),
                "address": request.form.get("address"),
                "email": request.form.get("email"),
                "phone_number": request.form.get("phone_number"), 
                "is_urgent": is_urgent,
            }
            mongo.db.tasks.insert_one(task)

            msg = Message('Bokning mottagen', sender='info@nilssonsstadtjanst.se', recipients=[request.form.get("email")])
            msg.body = 'Du har bokat: {} \n description: {} \n Tid och datum: {} \n Address: {} \n email: {} \n Telefonnummer: {} \n'.format(request.form.get("category_name"),request.form.get("description"),request.form.get("date"),request.form.get("address"),request.form.get("email"),request.form.get("phone_number"))
            mail.send(msg)

            flash("Booking Successfully Updated")
            return redirect(url_for("index"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_task.html", categori=categories)


@app.route("/update_task/<task_id>", methods=["GET", "POST"]) 
def update_task(task_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "description": request.form.get("description"),
            "date": request.form.get("date"),
            "address": request.form.get("address"),
            "phone_number": request.form.get("phone_number"), 
            "is_urgent": is_urgent,
            "created_by": session["user"]
        }
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit)
        flash("Booking Successfully Updated")
        return redirect(url_for("index"))
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})   
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("update_task.html", task=task, categori=categories)


@app.route("/delete_task/<task_id>", methods=["POST"])
def delete_task(task_id): 
    if request.method == "POST":
        mongo.db.tasks.remove({"_id": ObjectId(task_id)})
        flash("Booking Successfully Deleted")
    return redirect(url_for("index"))    


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
