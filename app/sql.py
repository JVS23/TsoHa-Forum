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