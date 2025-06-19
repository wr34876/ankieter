from . import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    # relacja: jedna kategoria -> wiele ankiet
    polls = db.relationship('Poll', backref='category', lazy=True)