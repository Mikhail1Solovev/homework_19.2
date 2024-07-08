import json
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def handle(self, *args, **options):
        # Удаление всех продуктов и категорий
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Чтение данных из файлов фикстур
        categories = self.json_read('catalog/fixtures/categories.json')
        products = self.json_read('catalog/fixtures/products.json')

        # Создание категорий
        category_objs = [Category(**cat) for cat in categories]
        Category.objects.bulk_create(category_objs)

        # Создание продуктов
        product_objs = [
            Product(
                name=prod['name'],
                description=prod['description'],
                image=prod['image'],
                category=Category.objects.get(pk=prod['category']),
                price=prod['price'],
                created_at=prod['created_at'],
                updated_at=prod['updated_at'],
                manufactured_at=prod['manufactured_at'],
            ) for prod in products
        ]
        Product.objects.bulk_create(product_objs)
