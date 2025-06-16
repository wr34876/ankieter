from . import db

class AnswerOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'), nullable=False)
    votes = db.Column(db.Integer, default=0)

    # Opcjonalnie relacja w stronę Poll (dla wygody)
    poll = db.relationship('Poll', backref=db.backref('answer_options', lazy=True))