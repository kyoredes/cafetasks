s:
	uv run python manage.py runserver
start:
	uv run python manage.py runserver
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