from flask import redirect, render_template, request, session
from sqlalchemy.sql import text


def send(db, title, content):

    user_id = session.get("user_id")

    sql = text("INSERT INTO threads (title, content, likes, user_id, created_at) VALUES (:title, :content, 0, :user_id, NOW())")
    db.session.execute(sql, {"title":title, "content":content, "user_id":user_id})
    db.session.commit()
    return True