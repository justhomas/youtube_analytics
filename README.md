# Youtube Analytics

MVP for Avkash Chauhan

## Running the project

### Using Docker

* Update the `.env` file with correct path for SQlite.
* Make sure `sqlalchemy.url` in `alembic.ini` is same as the path in `.env`
* Ensure that docker is installed
* Run the following command `docker-compose up`
* Download and paste the data into `/app/data` in the docker container
* run `python/load_data.py` to load the data into database

### Without using Docker.
* create python virtual environment
`python -m venv venv`
* install requirements
`pip install -r requirements.txt`
* create tables using alembic
`alembic upgrade head` 
* Download and paste the data into `/app/data` in the docker container
* run `python/load_data.py` to load the data into database
* Run the project `uvicorn app.main:app --reload`


### API Documentation

http://127.0.0.1:8000/docs#/







