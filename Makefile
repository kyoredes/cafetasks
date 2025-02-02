dev:
	uv run python manage.py runserver
start:
	uv run gunicorn --bind 0.0.0.0:8000 cafetasks.wsgi
m:
	uv run python manage.py makemigrations
	uv run python manage.py migrate
migrate:
	uv run python manage.py makemigrations
	uv run python manage.py migrate
indx:
	uv run python manage.py search_index --rebuild
sh:
	uv run python manage.py shell