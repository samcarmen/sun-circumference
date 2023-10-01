# Start the Redis server
start-redis:
	brew services start redis

# Start the Celery worker in the background
start-celery:
	celery -A sun_circumference worker --loglevel=info &

# Launch the Django shell and execute the compute_pi_indefinitely.delay() command
run-pi-task:
	echo "from pi_calculator.utils import compute_pi_indefinitely; compute_pi_indefinitely.delay()" | python manage.py shell

# Start the Django development server
start-django:
	python manage.py runserver &

# Main command to start Redis, the Celery worker, the compute_pi_indefinitely task, and the Django server
start: start-redis start-celery run-pi-task start-django

# Stop Redis, Celery, and Django server
stop-redis:
	brew services stop redis

stop-celery:
	pkill -f "celery worker"

stop-django:
	kill $(lsof -t -i:8000)

stop: stop-redis stop-celery stop-django

# Restart everything (Stop + Start)
restart: stop start