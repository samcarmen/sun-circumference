# Naluri Space Project

Welcome to the Naluri Space Project web application. This project is designed to calculate the value of Pi with increasing accuracy. Using the most precise value of Pi we derive, the application then determines the circumference of the sun.


## Features:

- Calculates the value of π to increasing accuracy using the Chudnovsky algorithm.
- Stores the most accurate value of π in Redis for fast retrieval.
- Uses Django REST framework to serve the latest computed values.
- Utilizes Celery for background computation tasks.

## Prerequisites:

- Python (3.11 or higher)
- Redis server

## Setup & Installation:

1. **Clone the repository:**

   ```
   git clone https://github.com/samcarmen/sun-circumference.git
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


## Run the project:

The `Makefile` provided in this project simplifies the process of starting, stopping, and restarting the necessary services for this application. Below are the available commands:

1. **Start Services:**

   This command will start Redis, Celery, and the Django server. It also triggers the `compute_pi_indefinitely` function to begin calculating π.

   ```
   make start
   ```

2. **Stop Services:**

   Use this command to gracefully shut down all running services initiated by the `start` command.

   ```
   make stop
   ```

3. **Restart Services:**

   If you need to refresh all services, use this command. It will stop and then restart all the services.

   ```
   make restart
   ```

## Usage:

1. **Visit the Homepage:**

   Open your browser and navigate to `http://127.0.0.1:8000/`. The homepage will display the latest known value of π and the computed circumference of the sun.

2. **View API Endpoints:**

   To retrieve the latest value of π and the circumference of the sun, navigate to `http://127.0.0.1:8000/sun_circumference/`.
