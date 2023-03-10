from db import db
from sqlalchemy import text

def get_threads():
    result = db.session.execute(text("SELECT threads.id, \
             title, content, likes, created_at, user_id, username \
             FROM threads LEFT JOIN users ON threads.user_id = users.id ORDER BY threads.id DESC"))
    return result.fetchall()

def get_threads_by_category(category_id):
    sql = text("SELECT threads.id, \
          title, content, likes, created_at, user_id, username \
          FROM threads LEFT JOIN users ON threads.user_id = users.id WHERE category_id=:category_id ORDER BY threads.id DESC")
    result = db.session.execute(sql, {"category_id":category_id})
    return result.fetchall()

def select_thread(id):
    sql = text("SELECT threads.id, title, content, user_id, created_at, \
          likes, username FROM threads LEFT JOIN users ON user_id = users.id WHERE threads.id=:id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()

def get_replies(id):
    sql = text("SELECT replies.content, sent_at, username \
          FROM replies LEFT JOIN threads ON thread_id = threads.id LEFT JOIN users ON replies.user_id = users.id WHERE threads.id=:id ORDER BY replies.id ASC;")
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def new_thread(title, content, user_id, category, formatted_date):
    sql = text("INSERT INTO threads (title, content, likes, user_id, category_id, created_at) VALUES (:title, :content, 0, :user_id, :category_id, :created_at)")
    db.session.execute(sql, {"title":title, "content":content, "user_id":user_id, "category_id":category, "created_at":formatted_date})
    db.session.commit()
    return True

def new_reply(content, user_id, thread_id, formatted_date):
    sql = text("INSERT INTO replies (content, user_id, sent_at, thread_id) VALUES (:content, :user_id, :sent_at, :thread_id)")
    db.session.execute(sql, {"content":content, "user_id":user_id, "thread_id":thread_id, "sent_at":formatted_date})
    db.session.commit()
    return True

def new_like(user_id, thread_id):
    sql = text("INSERT INTO likes (liker_id, thread_id) VALUES (:user_id, :thread_id)")
    try: 
        db.session.execute(sql, {"user_id":user_id, "thread_id":thread_id})
        db.session.commit()
    except:
        return False
    return True

def update_likes(thread_id):
    sql = text("UPDATE threads SET likes = likes + 1 WHERE id=:thread_id")
    db.session.execute(sql, {"thread_id":thread_id})
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
