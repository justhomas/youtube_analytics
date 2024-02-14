FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app/

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./app /app/app
