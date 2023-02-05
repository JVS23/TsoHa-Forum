from os import getenv
from flask import Flask
from flask import redirect, render_template, request, session, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from app import app
import threads

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html") 


@app.route("/home")
def home():
    result = db.session.execute(text("SELECT threads.id, title, content, likes, created_at, user_id, username FROM threads LEFT JOIN users ON threads.user_id = users.id ORDER BY threads.id DESC"))
    threads = result.fetchall()
    return render_template("home.html", threads=threads)

@app.route("/thread/<int:id>")
def thread(id):
    sql = text("SELECT * FROM threads WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    thread_info = result.fetchone()
    return render_template("thread.html", thread_info=thread_info)


@app.route("/send", methods=["POST"])
def send():
    title = request.form["title"]
    content = request.form["content"]

    if threads.send(db, title, content):
        return redirect("/home")
    else:
        return render_template("error.html", message="Could not create thread")



@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return render_template("error.html", message="No such username or password")
    if not check_password_hash(user[1], password):
        return render_template("error.html", message="No such username or password")
    

    session["username"] = username
    session["user_id"] = user[0]

    return redirect("/home")


@app.route("/logout")
def logout():
    del session["username"]
    del session["user_id"]
    return redirect("/")


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

    flash('Your account was successfully created! You can now log in.')
    return redirect("/")


@app.route("/new")
def new():
    return render_template("new.html")


@app.route("/error")
def error():
    return render_template("error.html")

