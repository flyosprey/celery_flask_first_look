from project.extensions import my_celery, db
from sqlalchemy import text


@my_celery.celery.task
def add_number_as_user(number):
    print("In task")
    query_string = "INSERT INTO user (name) VALUES (:name)"
    query_text = text(query_string)
    query = query_text.bindparams(name=number)
    db.session.execute(query)
    db.session.commit()
    return 'DONE!'
