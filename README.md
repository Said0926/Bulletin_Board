# Bulletin Board — Фанатская доска объявлений для MMORPG сервера

Веб-приложение на Django для фанатского сервера MMORPG. Пользователи могут публиковать объявления по категориям, оставлять отклики и получать email-уведомления.

## Стек

- Python 3.x / Django
- django-ckeditor (rich text с загрузкой изображений)
- Bootstrap 5
- SQLite (разработка)

## Функциональность

- Регистрация по email с подтверждением через код
- Создание, редактирование и удаление объявлений
- Rich text редактор с поддержкой изображений и видео
- Категории объявлений: Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний
- Отклики на объявления
- Приватная страница с откликами — фильтрация, принятие и удаление
- Email-уведомления при новом отклике и при принятии
- Новостная рассылка для подписанных пользователей

## Установка

```bash
git clone https://github.com/Said0926/Bulletin_Board.git
cd Bulletin_Board

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Структура приложений

```
users/       — кастомный User, авторизация по email
bulletins/   — объявления и отклики
newsletter/  — новостная рассылка
```

## Настройки

В `settings.py` для разработки используется:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Для продакшена замените на SMTP-бэкенд с реальными данными.
