from flask import Blueprint, jsonify
from celery.result import AsyncResult
from .extensions import my_celery as celery
from .tasks import add_user
from project_example.tasks import MyTask

main = Blueprint('main', __name__)


@main.route('/na/<name>')
def start_name(name):
    print("Start celery task")
    task = add_user.delay(name)
    return f"Result: {task.id}"


@main.route('/nu/<number>')
def start_number(number):
    print("Start celery task")
    task = MyTask().delay(number)
    return f"Result: {task.id}"


@main.route('/cancel/start_name/<task_id>')
def cancel(task_id):
    task = add_user.AsyncResult(task_id)
    task.abort()
    return 'Canceled!'


@main.route('/<task_id>')
def status(task_id):
    task_result = AsyncResult(task_id, app=celery.celery)
    if task_result.state == 'PENDING':
        response = {
            'status': 'pending'
        }
    elif task_result.state == 'SUCCESS':
        response = {
            'status': 'complete',
            'result': task_result.result
        }
    else:
        response = {
            'status': 'incomplete',
            'result': task_result.result or "NONE"
        }
    return jsonify(response)
