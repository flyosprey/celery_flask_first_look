from project import create_app

app, celery = create_app()
app.app_context().push()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
