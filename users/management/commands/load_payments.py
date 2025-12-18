import os
from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Заполнение БД фикстурой
    """

    def handle(self, *args: list, **kwargs: dict) -> None:
        # Удаление всех объектов, если это необходимо
        # Уберите или измените следующую строку в зависимости от вашей логики
        # SomeModel.objects.all().delete()

        call_command('loaddata', 'data.json')  # Измените имя файла на нужное

        self.stdout.write(self.style.SUCCESS("Фикстуры из файла data.json успешно загружены"))
