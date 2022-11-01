import csv
from pathlib import Path

from django.core.management.base import BaseCommand

from recipes.models import Ingredient

from foodgram.settings import BASE_DIR

PROJECT_DIR = Path(BASE_DIR).resolve().parent.joinpath('data')
FILE_TO_OPEN = PROJECT_DIR / "ingredients.csv"


class Command(BaseCommand):
    help = "Импорт ингредиентов в БД"

    def handle(self, **kwargs):
        with open(
                FILE_TO_OPEN, "r", encoding="UTF-8"
        ) as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                Ingredient.objects.get_or_create(
                    name=row['name'],
                    measurement_unit=row['measurement_unit']
                )
