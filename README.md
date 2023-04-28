# HOW TO RUN?


## You need run each command in the new terminal window
<ul>
    <li>flask --app run.py run -> Run flask app</li>
    <li>celery -A run.celery worker --loglevel=info -E --pool=solo -> Run celery worker</li>
    <li>celery -A run.celery flower --port=5555 -> Run flower UI</li>
</ul>
