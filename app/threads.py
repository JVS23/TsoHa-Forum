from flask import redirect, render_template, request, session
from datetime import datetime
import sql


def send(title, content):

    user_id = session.get("user_id")
    time = datetime.now()
    formatted_date = time.strftime("%d.%m.%Y %H:%M:%S")
    sql.new_thread(title, content, user_id, formatted_date)

    return True