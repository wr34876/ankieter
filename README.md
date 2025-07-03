![CI/CD Status](https://github.com/wr34876/ankieter/actions/workflows/deploy.yml/badge.svg)

# Ankieter

Prosta aplikacja webowa do tworzenia i głosowania w ankietach, przygotowana w ramach projektu zaliczeniowego z przedmiotu *Narzędzia do automatyzacji budowy oprogramowania*.

## 🧩 Opis

Aplikacja umożliwia:
- tworzenie własnych ankiet z wieloma odpowiedziami,
- głosowanie na wybraną opcję,
- przeglądanie wyników ankiety,
- przypisywanie ankiet do kategorii tematycznych,
- zostawianie opinii o aplikacji poprzez prosty formularz feedbacku.

Projekt został podzielony na kilka modułów, z wykorzystaniem dobrych praktyk Flaskowych (modularna struktura, szablony, testy jednostkowe, CI/CD).

---

## 🚀 Technologie

- **Python 3.x**
- **Flask**
- **Flask-SQLAlchemy** (ORM)
- **SQLite** (baza danych)
- **Jinja2** (szablony HTML)
- **Bootstrap 5** (frontend)
- **pytest** (testy jednostkowe)
- **GitHub + GitHub Actions** (CI/CD)
- **Render.com** (hosting)

---

## 📦 Struktura katalogów

<pre markdown="1">
Ankieter/
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── models/
│ │ ├── poll.py
│ │ ├── category.py
│ │ ├── answer_option.py
│ │ ├── user_feedback.py # nowy model opinii użytkowników
│ ├── templates/
│ │ ├── index.html
│ │ ├── list.html
│ │ ├── create_poll.html
│ │ ├── feedback_form.html # formularz opinii
│ │ ├── feedback_thanks.html
│ │ ├── view_poll.html
│ └── static/
│ │ ├── style.css
├── tests/
│ ├── test_routes.py
│ ├── test_poll.py
│ ├── test_poll_flow.py
│ ├── conftest.py
│ ├── test_answer_option.py
│ ├── test_basic.py
│ ├── test_category.py
│ ├── test_create_poll.py # testy formularza tworzenia ankiet
│ ├── test_feedback.py # testy funkcjonalności feedbacku
├── run.py
├── requirements.txt
└── README.md
</pre>

---

## 🧠 Funkcjonalności

### ✅ Modele

1. **Poll** – ankieta zawierająca pytanie, datę utworzenia i powiązanie z kategorią.
2. **AnswerOption** – możliwe odpowiedzi powiązane z ankietą, zawierają tekst i licznik głosów.
3. **Vote** – reprezentuje oddany głos.
4. **Category** – opcjonalne kategorie tematyczne grupujące ankiety.
5. **UserFeedback** – formularz do zostawiania opinii o aplikacji.

### ✅ Widoki

1. **Strona główna** – lista ankiet i nawigacja.
2. **Stwórz ankietę** – formularz tworzenia nowej ankiety.
3. **Głosowanie w ankiecie** – wybór odpowiedzi i oddanie głosu.
4. **Wyniki ankiety** – prezentacja wyników głosowania.
5. **Opinie o aplikacji** – prosty formularz feedbacku.

---

## 🧪 Testy

Testy jednostkowe realizowane przy użyciu `pytest`. Testy znajdują się w katalogu `tests/` i pokrywają:

- **Podstawowe widoki** (`/polls`, `/polls/<id>/options`, `/categories`),
- **Obsługę tworzenia ankiet** (formularz GET i POST, walidacja danych),
- **Głosowanie** (w tym testy poprawnego i niepoprawnego głosowania),
- **Formularz opinii** (formularz GET i POST, walidacja),
- **Obsługę błędów** (np. 404 dla nieistniejących zasobów).

Aby je uruchomić należy wpisać komendę:

```bash
pytest
```
Przykładowy test widoku:
```python
def test_index_page(client):
    response = client.get('/polls')
    assert response.status_code == 200
    assert b"Testowe pytanie?" in response.data
```

Testy uruchamiają się na bazie SQLite w pamięci, co pozwala na izolację od danych produkcyjnych.

---

## ⚙️ CI/CD

Projekt zawiera zautomatyzowane testowanie oraz proces wdrażania za pomocą GitHub Actions. Po każdej aktualizacji repozytorium na GitHub:
- uruchamiane są testy automatyczne,
- jeśli testy przejdą pomyślnie, następuje automatyczny deploy na Render.com.

---

## 👥 Zespół projektowy

- **Paweł Białecki** – lider zespołu, integracja kodu, konfiguracja CI/CD, szkielet aplikacji
- **Kacper Frączyk** – modele danych
- **Marek Stangryciuk** – testy i dokumentacja
- **Jan Łachacz** – frontend i widoki HTML

---

## 📌 Status projektu

🔨 Projekt w trakcie realizacji – aktualnie w fazie szkieletu aplikacji.  
Kolejne funkcje są sukcesywnie dodawane zgodnie z harmonogramem i podziałem prac.

---

## 📄 Licencja

Projekt edukacyjny, brak licencji produkcyjnej.

