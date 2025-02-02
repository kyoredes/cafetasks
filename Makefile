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
sh:
	uv run python manage.py shell
urls:
	uv run python manage.py show_urls