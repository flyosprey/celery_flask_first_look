from .extensions import my_celery
from .db import db
from sqlalchemy import text


@my_celery.celery.task
def add_user(name):
    print("In task")
    query_string = "INSERT INTO user (name) VALUES (:name)"
    query_text = text(query_string)
    query = query_text.bindparams(name=name)
    db.session.execute(query)
    db.session.commit()
    return 'DONE!'
