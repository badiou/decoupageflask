
# TODO
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv

load_dotenv()
password=quote_plus(os.getenv('PASSWORD_DB'))
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:{}@localhost:5432/session4_sunday'.format(password)
SQLALCHEMY_TRACK_MODIFICATIONS = False