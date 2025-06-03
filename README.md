# Ankieter

Prosta aplikacja webowa do tworzenia i głosowania w ankietach, przygotowana w ramach projektu zaliczeniowego z przedmiotu *Narzędzia do automatyzacji budowy oprogramowania*.

## 🧩 Opis

Aplikacja umożliwia:
- tworzenie własnych ankiet z wieloma odpowiedziami,
- głosowanie na wybraną opcję,
- przeglądanie wyników ankiety,
- przypisywanie ankiet do kategorii tematycznych,
- zostawianie opinii o aplikacji.

Projekt został podzielony na kilka modułów, z wykorzystaniem dobrych praktyk Flaskowych (modularna struktura, szablony, testy jednostkowe, CI/CD).

---

## 🚀 Technologie

- **Python 3.x**
- **Flask**
- **SQLite** (baza danych)
- **Jinja2** (szablony HTML)
- **Bootstrap 5** (frontend)
- **pytest** (testy)
- **GitHub + GitHub Actions** (CI/CD)
- **Render.com** (hosting)

---

## 📦 Struktura katalogów

Ankieter/
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── models.py
│ ├── templates/
│ └── static/
├── tests/
├── run.py
├── requirements.txt
└── README.md


---

## 🧠 Funkcjonalności

### ✅ Modele

1. **Poll** – ankieta zawierająca pytanie i datę utworzenia.
2. **AnswerOption** – możliwe odpowiedzi powiązane z ankietą.
3. **Vote** – reprezentuje oddany głos.
4. **Category** – opcjonalne kategorie tematyczne dla ankiet.
5. **UserFeedback** – formularz do zostawiania opinii o aplikacji.

### ✅ Widoki

1. **Strona główna** – lista ankiet i nawigacja.
2. **Stwórz ankietę** – formularz tworzenia nowej ankiety.
3. **Głosowanie w ankiecie** – wybór odpowiedzi i oddanie głosu.
4. **Wyniki ankiety** – prezentacja wyników głosowania.
5. **Opinie o aplikacji** – prosty formularz feedbacku.

---

## 🧪 Testy

Testy jednostkowe realizowane przy użyciu `pytest` (znajdują się w folderze `tests/`).

---

## ⚙️ CI/CD

Projekt zawiera zautomatyzowane testowanie oraz proces wdrażania za pomocą GitHub Actions. Po każdym pushu do repo:
- uruchamiane są testy,
- jeśli zakończą się sukcesem – projekt jest deployowany na Render.com.

---

## 👥 Zespół projektowy

- **Paweł Białecki** – lider zespołu, integracja kodu, konfiguracja CI/CD, szkielet aplikacji
- **Kacper Frączyk** – modele danych
- **Marek Stangryciuk** – testy i dokumentacja
- **Jan Łachacz** – frontend i widoki HTML

---

## 📌 Status projektu

🔨 Projekt w trakcie realizacji – aktualnie w fazie szkieletu aplikacji.  
Kolejne funkcje będą dodawane zgodnie z podziałem prac.

---

## 📄 Licencja

Projekt edukacyjny, brak licencji produkcyjnej.

