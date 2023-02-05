from flask import redirect, render_template, request, session
from sqlalchemy.sql import text
from datetime import datetime


def send(db, title, content):

    user_id = session.get("user_id")
    time = datetime.now()

    formatted_date = time.strftime("%d.%m.%Y %H:%M:%S")

    sql = text("INSERT INTO threads (title, content, likes, user_id, created_at) VALUES (:title, :content, 0, :user_id, :created_at)")
    db.session.execute(sql, {"title":title, "content":content, "user_id":user_id, "created_at":formatted_date})
    db.session.commit()
    return True