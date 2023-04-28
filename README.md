# HOW TO RUN?


#### First of all need to run redis
<ul>
    <li>docker run --name my-redis -p 6379:6379 -d redis</li>
</ul>

<hr>

#### Then you need run each command in the new terminal window
<ul>
    <li>flask --app run.py run -> Run flask app</li>
    <li>celery -A run.celery worker --loglevel=info -E --pool=solo -> Run celery worker</li>
    <li>celery -A run.celery flower --port=5555 -> Run flower UI</li>
</ul>
