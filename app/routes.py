from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from .models.poll import Poll
from .models.answer_option import AnswerOption
from .models.category import Category
from .models.user_feedback import UserFeedback

main = Blueprint('main', __name__)


@main.route('/')
def index():
    """Strona główna - wyświetla listę wszystkich ankiet"""
    polls = Poll.query.order_by(Poll.created_at.desc()).all()
    return render_template('index.html', polls=polls)


@main.route('/polls/create', methods=['GET', 'POST'])
def create_poll():
    """Tworzenie nowej ankiety"""
    if request.method == 'POST':
        question = request.form.get('question')
        options = request.form.getlist('options[]')

        # Podstawowa walidacja
        if not question or len(options) < 2:
            return "Wypełnij pytanie i dodaj minimum 2 opcje odpowiedzi", 400

        try:
            # Tworzenie nowej ankiety
            poll = Poll(question=question)
            db.session.add(poll)
            db.session.flush()  # Pobieramy ID ankiety

            # Dodawanie opcji odpowiedzi
            for option_text in options:
                if option_text.strip():  # Pomijamy puste opcje
                    option = AnswerOption(
                        text=option_text.strip(),
                        poll_id=poll.id
                    )
                    db.session.add(option)

            db.session.commit()
            return redirect(url_for('main.index'))

        except Exception as e:
            db.session.rollback()
            return f"Wystąpił błąd podczas tworzenia ankiety: {str(e)}", 500

    # Wyświetlanie formularza (GET)
    return render_template('create_poll.html')


@main.route('/polls/<int:poll_id>')
def view_poll(poll_id):
    """Wyświetlanie pojedynczej ankiety"""
    poll = Poll.query.get_or_404(poll_id)
    options = AnswerOption.query.filter_by(poll_id=poll_id).all()
    return render_template('view_poll.html', poll=poll, options=options)


@main.route('/polls')
def list_polls():
    """Lista wszystkich ankiet"""
    polls = Poll.query.order_by(Poll.created_at.desc()).all()
    return render_template('list.html', polls=polls)


@main.route('/polls/<int:poll_id>/vote', methods=['POST'])
def vote(poll_id):
    """Obsługa głosowania w ankiecie"""
    poll = Poll.query.get_or_404(poll_id)
    selected_option_id = request.form.get('answer')

    if not selected_option_id:
        return "Nie wybrano odpowiedzi", 400

    try:
        selected_option_id = int(selected_option_id)

    except ValueError:
        return "Nieprawidłowa opcja odpowiedzi", 400

    selected_option = AnswerOption.query.get(selected_option_id)
    if selected_option is None:
        # Opcja nie istnieje - zwracamy 404
        return "Opcja odpowiedzi nie istnieje", 404

    if selected_option.poll_id != poll.id:
        return "Nieprawidłowa opcja odpowiedzi dla tej ankiety", 400

        # selected_option = AnswerOption.query.get_or_404(selected_option_id)
        #if selected_option is None:
            # Opcja odpowiedzi nie istnieje - zwracamy 404
         #   return "Opcja odpowiedzi nie istnieje", 404

        #if selected_option.poll_id != poll_id:
        #    return "Nieprawidłowa opcja odpowiedzi", 400
    try:
        selected_option.votes += 1
        db.session.commit()

        return redirect(url_for('main.view_poll', poll_id=poll_id))
    except Exception as e:
        db.session.rollback()
        return f"Wystąpił błąd podczas głosowania: {str(e)}", 500


@main.route('/categories')
def list_categories():
    """Lista wszystkich kategorii"""
    categories = Category.query.all()
    return render_template('list.html', categories=categories)

@main.route('/polls/<int:poll_id>/delete', methods=['POST'])
def delete_poll(poll_id):
    """Usuwanie ankiety i jej opcji"""
    poll = Poll.query.get_or_404(poll_id)
    # Usuwamy powiązane opcje odpowiedzi
    for option in poll.answer_options:
        db.session.delete(option)
    db.session.delete(poll)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        message = request.form.get('message', '')
        if not message.strip():
            return "Wiadomość nie może być pusta.", 400

        feedback = UserFeedback(message=message.strip())
        db.session.add(feedback)
        db.session.commit()
        return render_template('feedback_thanks.html')

    return render_template('feedback_form.html')
