from db import db
from sqlalchemy import text

def get_threads():
    result = db.session.execute(text("SELECT threads.id, \
        title, content, likes, created_at, user_id, username \
        FROM threads LEFT JOIN users ON threads.user_id = users.id ORDER BY threads.id DESC"))
    return result.fetchall()

def select_thread(id):
    sql = text("SELECT * FROM threads WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()

def new_thread(title, content, user_id, formatted_date):
    sql = text("INSERT INTO threads (title, content, likes, user_id, created_at) VALUES (:title, :content, 0, :user_id, :created_at)")
    db.session.execute(sql, {"title":title, "content":content, "user_id":user_id, "created_at":formatted_date})
    db.session.commit()
    return True

def get_user_logins(username):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    return result.fetchone()

def create_user(username, hash_value):
    sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()
    return True