from flask import redirect, render_template, request, session
from datetime import datetime
import sql


def send(title, content, category):

    user_id = session.get("user_id")
    time = datetime.now()
    formatted_date = time.strftime("%d.%m.%Y %H:%M:%S")
    sql.new_thread(title, content, user_id, category, formatted_date)

    return True

def send_reply(content, thread_id):

    user_id = session.get("user_id")
    time = datetime.now()
    formatted_date = time.strftime("%d.%m.%Y %H:%M:%S")
    sql.new_reply(content, user_id, thread_id, formatted_date)

    return True