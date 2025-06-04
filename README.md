1. Установка зависимостей
1.Клонировать репозиторий:
       git clone https://github.com/peshkadd/WebDDS2.git
       cd WebDDS
    1. Создайте и активируйте виртуальное окружение:
        ◦ Для Windows:
          python -m venv .venv
          .venv\Scripts\activate
        ◦ Для Linux/macOS:
          python3 -m venv .venv
          source .venv/bin/activate
    2. Установить зависимости:
       pip install -r requirements.txt
2. Настройка базы данных
    1. Примените миграции (SQLite создастся автоматически):
       python manage.py migrate
    2. Создайте суперпользователя(для доступа в админку):
       python manage.py createsuperuser
       Укажите email, логин и пароль.
3. Запуск веб-сервиса
    1. Запустите сервер разработки:
       python manage.py runserver
    2. Откройте в браузере:
        ◦ Основное приложение: http://127.0.0.1:8000/
        ◦ Админ-панель: http://127.0.0.1:8000/admin/
    3. (Для production) Настройте WSGI:
Конфигурация для Nginx/Apache находится в WebDDS2/wsgi.py
Дополнительные команды
    • Создание новых миграций (при изменении моделей):
      python manage.py migrate
    • Запуск тестов:
      python manage.py test
    • Сбор статики (для production):
      python manage.py collectstatic
Требования к системе
    • Python 3.9+
    • Django 4.2+
    • SQLite 3.8+ (или PostgreSQL/MySQL для production)

