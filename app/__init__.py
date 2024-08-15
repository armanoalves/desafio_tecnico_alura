from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('USER_NAME')}:{os.getenv('PASSWORD')}@{os.getenv('HOST')}:{os.getenv('PORT')}/{os.getenv('DATABASE')}"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controllers import default
from app.models import tabelas
