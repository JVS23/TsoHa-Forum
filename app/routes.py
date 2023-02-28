from os import getenv
from flask import Flask
from flask import redirect, render_template, request, session, flash, abort
from werkzeug.security import check_password_hash, generate_password_hash, secrets
import threads
import sql
from app import app



@app.route("/")
def index():
    try:
        session["username"]
        return redirect("/home")
    except:
        return render_template("index.html") 


@app.route("/home")
def home():
    threads = sql.get_threads()
    return render_template("home.html", threads=threads)


@app.route("/thread/<int:id>")
def thread(id):
    thread_info = sql.select_thread(id)
    return render_template("thread.html", thread_info=thread_info)


@app.route("/send", methods=["POST"])
def send():
    title = request.form["title"]
    content = request.form["content"]

    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    if len(title) > 100:
        return render_template("error.html", message="The title is too long")
    if len(content) > 10000:
        return render_template("error.html", message="Content of the post is too long")
    if threads.send(title, content):
        return redirect("/home")
    else:
        return render_template("error.html", message="Could not create thread")


@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    user = sql.get_user_logins(username)
    if not user:
        return render_template("error.html", message="No such username or password")
    if not check_password_hash(user[1], password):
        return render_template("error.html", message="No such username or password")
    
    session["username"] = username
    session["user_id"] = user[0]
    session["csrf_token"] = secrets.token_hex(16)

    return redirect("/home")


@app.route("/logout")
def logout():
    del session["username"]
    del session["user_id"]
    del session["csrf_token"]
    return redirect("/")


@app.route("/create",methods=["POST"])
def create():
    username = request.form["username"]
    password = request.form["password"]
    hash_value = generate_password_hash(password)

    if len(username) > 20 or len(username) < 2:
        return render_template("error.html", message="Username length must be between 2-20 characters")
    if len(password) > 51 or len(password) < 2:
        return render_template("error.html", message="Password length needs to be within 2-50 characters")
    try:
        sql.create_user(username, hash_value)
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
