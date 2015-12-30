import os
from flask_appbuilder.security.manager import AUTH_DB

BASEDIR = os.path.abspath(os.path.dirname(__file__))

APP_THEME = "yeti.css"
APP_NAME = "Testing!"

MONGODB_SETTINGS = {'host': "mongodb://MongoLab-m:U3SMzPi3jCQ8Gu9fUmOpX0sKXAw5KGwlXhGmwAewW4M-@ds054118.mongolab.com:54118/MongoLab-m"}
SECRET_KEY = "56826f06902a4ab42713807b"

AUTH_TYPE = AUTH_DB
AUTH_ROLE_ADMIN = "Admin"
AUTH_ROLE_PUBLIC = "Public"
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Public"