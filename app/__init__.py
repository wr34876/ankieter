from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .models.poll import Poll
from .models.answer_option import AnswerOption
from .models.category import Category
from .models.user_feedback import UserFeedback

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///polls.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app