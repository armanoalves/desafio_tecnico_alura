import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True

SQLALCHEMY_DATABASE_URI= f"postgresql://{os.getenv('USER_NAME')}:{os.getenv('PASSWORD')}@{os.getenv('HOST')}:{os.getenv('PORT')}/{os.getenv('DATABASE')}"
SQLALCHEMY_TRACK_MODIFICATIONS = True