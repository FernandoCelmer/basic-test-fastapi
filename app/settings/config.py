import os

from distutils.util import strtobool
from dotenv import load_dotenv

env = load_dotenv()

DEBUG = bool(strtobool(os.environ.get("DEBUG")))
ENVIRONMENT = os.environ.get("ENVIRONMENT")
DATABASE_URL = os.environ.get("DATABASE_URL")
SECRET_KEY = os.environ.get("SECRET_KEY")
HOST = os.environ.get("HOST")
PORT = int(os.environ.get("PORT"))


if ENVIRONMENT in ('dev', 'prod'):
    ROOT_PATH = "/{}/".format(ENVIRONMENT)
else:
    ROOT_PATH = "/"
