from os import getenv
from flask import Flask
from flask import redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from app import app

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


@app.route("/")
def index():

    return render_template("index.html") 

@app.route("/home")
def home():
    result = db.session.execute(text("SELECT content FROM messages"))
    messages = result.fetchall()
    return render_template("home.html", count=len(messages), messages=messages) 


@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    sql = text("SELECT password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return render_template("error.html", message="No such username or password")
    if not check_password_hash(user[0], password):
        return render_template("error.html", message="No such username or password")
    

    session["username"] = username
    return redirect("/home")

@app.route("/create",methods=["POST"])
def create():
    username = request.form["username"]
    password = request.form["password"]
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return render_template("error.html", message="Username already taken")

    session["username"] = username

    
    print("User created")
    return redirect("/home")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/error")
def error():
    return render_template("error.html")


@app.route("/new")
def new():
    return render_template("new.html")




@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    sql = text("INSERT INTO messages (content) VALUES (:content)")
    db.session.execute(sql, {"content":content})
    db.session.commit()
    return redirect("/")
