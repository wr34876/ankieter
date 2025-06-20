from flask import Blueprint, render_template, abort
from .models.poll import Poll
from .models.answer_option import AnswerOption
from .models.category import Category

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/polls')
def list_polls():
    polls = Poll.query.order_by(Poll.created_at.desc()).all()
    return render_template('templates/list.html', polls=polls)

@main.route('/polls/<int:poll_id>/options')
def list_options(poll_id):
    poll = Poll.query.get_or_404(poll_id)
    options = AnswerOption.query.filter_by(poll_id=poll_id).all()
    return render_template('templates/list.html', poll=poll, options=options)

@main.route('/categories')
def list_categories():
    categories = Category.query.all()
    return render_template('templates/list.html', categories=categories)