from django.core.management import BaseCommand

from catalog_app.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):


        category_list = [
            {'name': 'Фрукт', 'desc': 'Свежие из Астрахани'},
            {'name': 'Овощи', 'desc': 'Свежие из Грузии'},
            {'name': 'Ягоды', 'desc': 'Свежие из Турции'},
            {'name': 'Сухофрукты', 'desc': 'Свежие из Ташкента'},
            {'name': 'Маринад', 'desc': 'Из Абхазии'},
        ]

        category_for_create = []
        for category_id in category_list:
            category_for_create.append(
                Category(**category_id)
            )

        Category.objects.bulk_create(category_for_create)
