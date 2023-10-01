# Naluri Space Project

Explore the solar system with our advanced calculations. This project aims to calculate and display the circumference of the sun based on a continuously improving approximation of π.

## Features:

- Calculates the value of π to increasing accuracy using the Chudnovsky algorithm.
- Stores the most accurate value of π in Redis for fast retrieval.
- Uses Django REST framework to serve the latest computed values.
- Utilizes Celery for background computation tasks.

## Prerequisites:

- Python (3.11 or higher)
- Redis server
- RabbitMQ or another broker supported by Celery

## Setup & Installation:

1. **Clone the repository:**

   ```
   git clone https://your-repository-link.git
   cd sun_circumference
   ```

2. **Set up a virtual environment and install dependencies:**

   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up Redis:**

   Ensure you have Redis installed and running. 

   On macOS (using Homebrew):
   ```
   brew install redis
   brew services start redis
   ```

   On Ubuntu:
   ```
   sudo apt-get install redis-server
   redis-server &
   ```

   Make sure Redis is set up to persist data by checking or modifying its configuration. Typically, you'd ensure that either the RDB or AOF persistence option is enabled in the `redis.conf` file.

4. **Set up Celery:**

   We use Celery for background tasks. Ensure you have a broker like RabbitMQ installed or choose another supported broker.

   Start the Celery worker from the main project directory:
   
   ```
   celery -A your_project_name worker --loglevel=info
   ```

5. **Run the Django development server:**

   ```
   python manage.py runserver
   ```

## Usage:

1. **Visit the Homepage:**

   Open your browser and navigate to `http://127.0.0.1:8000/`. The homepage will display the latest known value of π and the computed circumference of the sun.

2. **View API Endpoints:**

   To retrieve the latest value of π and the circumference of the sun, navigate to `http://127.0.0.1:8000/sun_circumference/`.
