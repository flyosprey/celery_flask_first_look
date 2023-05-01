from celery import Celery
from project_example.tasks import MyTask


class MyCelery:
    def __init__(self, app=None):
        self.celery = Celery(__name__)
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.celery.conf.update(app.config)
        self.celery.conf.update(
            CELERY_QUEUES={
                'add': {'exchange': 'exchange1', 'routing_key': 'add'},
                'MyTask': {'exchange': 'exchange2', 'routing_key': 'MyTask'},
            },
            CELERY_DEFAULT_EXCHANGE_TYPE='direct',
            CELERY_DEFAULT_ROUTING_KEY='default',
            CELERY_ROUTES={
                'project.tasks.count': {'queue': 'add', 'routing_key': 'add'},
                'MyTask': {'queue': 'MyTask', 'routing_key': 'MyTask'},
            },
            CELERYD_CONCURRENCY=5,
            CELERY_RESULT_BACKEND='redis://localhost:6379/0',
            BROKER_URL='redis://localhost:6379/0',
        )

        self.celery.register_task(MyTask())

        class ContextTask(self.celery.Task):
            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return self.run(*args, **kwargs)

        self.celery.Task = ContextTask


my_celery = MyCelery()
