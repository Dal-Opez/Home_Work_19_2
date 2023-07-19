from django.core.management import BaseCommand

from catalog_app.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        products = [
            {'name': 'Абрикос', 'desc': 'Жёлтый', 'category_id': 1, 'price': '123'},
            {'name': 'Вишня', 'desc': 'Красная', 'category_id': 3, 'price': '456'},
            {'name': 'Салат', 'desc': 'Китайский', 'category_id': 2, 'price': '789'},
            {'name': 'Огурец', 'desc': 'Длинный', 'category_id': 2, 'price': '987'},
            {'name': 'Помидор', 'desc': 'Бычье сердце', 'category_id': 2, 'price': '654'},
            {'name': 'Арбуз', 'desc': 'Без косточек', 'category_id': 3, 'price': '321'},
            {'name': 'Изюм', 'desc': 'Обыкновенный', 'category_id': 4, 'price': '147'},
            {'name': 'Корнишон', 'desc': 'В банках', 'category_id': 5, 'price': '258'},
        ]

        products_for_create = []
        for prod in products:
            products_for_create.append(
                Product(**prod)
            )

        Product.objects.bulk_create(products_for_create)
