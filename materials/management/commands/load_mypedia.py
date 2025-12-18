import os
from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Заполнение БД фикстурами
    """

    def handle(self, *args: list, **kwargs: dict) -> None:
        # Получаем пути к файлам фикстур из переменных окружения или используем значения по умолчанию
        mypedia_fixture = os.getenv('MYPEDIA_FIXTURE', 'mypedia.json')
        payments_fixture = os.getenv('PAYMENTS_FIXTURE', 'payments.json')

        # Удаление объектов можно реализовать здесь, если нужно

        # Загружаем фикстуры
        call_command('loaddata', mypedia_fixture)
        call_command('loaddata', payments_fixture)

        self.stdout.write(self.style.SUCCESS(
            f"Фикстуры из файлов {mypedia_fixture} и {payments_fixture} успешно загружены"
        ))
