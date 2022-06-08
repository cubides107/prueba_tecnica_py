import psycopg2
from decouple import config
from flask_sqlalchemy import SQLAlchemy


def get_connection():
    return psycopg2.connect(
        host=config('PGSQL_HOST'),
        user=config('PGSQL_USER'),
        password=config('PGSQL_PASSWORD'),
        database=config('PGSQL_DATABASE')
    )
