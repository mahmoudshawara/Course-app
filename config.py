import os
from flask_sqlalchemy import SQLAlchemy
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
database = os.environ['POSTGRES_DB']
port = os.environ['POSTGRES_PORT']

SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'

#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost:5432/school'
SQLALCHEMY_TRACK_MODIFICATIONS = False

