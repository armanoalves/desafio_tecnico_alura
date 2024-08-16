from decouple import config

DEBUG = True

SQLALCHEMY_DATABASE_URI= f"postgresql://{config('DB_USERNAME')}:{config('DB_PASSWORD')}@{config('DB_HOST')}:{config('DB_PORT')}/{config('DB_DATABASE')}"
SQLALCHEMY_TRACK_MODIFICATIONS = True
