FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app/

# Copy and install requirements
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

# Copy the application code
COPY ./app /app/app
COPY ./data /app/data
COPY ./scripts /app/scripts
COPY ./tasks.py /app/tasks.py

COPY ./alembic /app/alembic
COPY ./alembic.ini /app/alembic.ini

# Expose the port the app runs on
EXPOSE 8000

# Create a start.sh file
COPY ./start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Set the default command to run the application using start.sh
CMD ["/app/start.sh"]
