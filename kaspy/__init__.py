from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# import learning_flashcards.views
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kasadmin@localhost/kas_erp'

db = SQLAlchemy()