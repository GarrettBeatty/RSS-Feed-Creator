init: flask db init
migrate: flask db migrate
upgrade: flask db upgrade
web: gunicorn rssfeedcreator.app:create_app\(\) -b 0.0.0.0:$PORT -w 3
