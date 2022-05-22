import os
import environ

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

env = environ.Env()
environ.Env.read_env(BASE_DIR+"/.env")

DEBUG = os.environ.get("DEBUG")
FASTAPI_ENV = os.environ.get("FASTAPI_ENV")
SQLALCHEMY_DATABASE_TEST_URL = os.environ.get("SQLALCHEMY_DATABASE_TEST_URL")
SQLALCHEMY_DATABASE_URL = os.environ.get("SQLALCHEMY_DATABASE_URL")