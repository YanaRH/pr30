# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код проекта
COPY . .

# Открываем порт (Django по умолчанию 8000)
EXPOSE 8000

# Команда для запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]