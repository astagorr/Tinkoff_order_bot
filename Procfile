web: gunicorn config.wsgi:application
worker: celery worker --app=tinkoff_order_bot.taskapp --loglevel=info
