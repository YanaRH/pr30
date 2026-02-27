# Django Project

## Описание
Проект на Django с API (DRF), JWT-аутентификацией, Celery, Redis и PostgreSQL.

## Запуск через Docker
1. Клонируйте репозиторий.
2. Создайте `.env` на основе `.env.example` и заполните переменные.
3. Запустите: `docker-compose up --build`.
4. Примените миграции: `docker-compose exec web python manage.py migrate`.
5. Создайте суперпользователя: `docker-compose exec web python manage.py createsuperuser`.

## Проверка работоспособности
- Веб: http://localhost:8000 (главная страница).
- Админка: http://localhost:8000/admin.
- API/Swagger: http://localhost:8000/swagger.
- БД: Проверьте подключение через админку или shell.
- Redis: `docker-compose exec redis redis-cli ping` (должен вернуть PONG).
- Celery: Проверьте логи: `docker-compose logs celery`.

## Структура
- `myproject/`: Настройки Django.
- `users/`, `catalog/`, `materials/`: Приложения
