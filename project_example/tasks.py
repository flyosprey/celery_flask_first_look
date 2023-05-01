from celery import Task
from sqlalchemy import text
from main_project.db import db


class MyTask(Task):
    name = "MyTask"

    def run(self, number):
        print("In task")
        query_string = "INSERT INTO user (name) VALUES (:name)"
        query_text = text(query_string)
        query = query_text.bindparams(name=number)
        db.session.execute(query)
        db.session.commit()
        return 'DONE!'
