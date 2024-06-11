from django.core.management import BaseCommand
import json
from catalog.models import Category, Product

file_fixture = 'products.json'


class Command(BaseCommand):

    @staticmethod
    def json_read_products(path_to_file):
        with open(path_to_file, "rt", encoding="UTF-8") as file:
            return json.load(file)  # Здесь мы получаем данные из фикстуры

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения
        # информации об одном объекте
        for category in Command.json_read_products(file_fixture):
            if category['model'] == 'catalog.category':
                category_for_create.append(
                    Category(pk=category['pk'],
                             name_category=category['fields']['name_category'],
                             description=category['fields']['description'])
                )
        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products(file_fixture):
            if product['model'] == 'catalog.product':
                product_for_create.append(
                    Product(pk=product['pk'],
                            name_product=product['fields']['name_product'],
                            description=product['fields']['description'],
                            image=product['fields']['image'],
                            category=Category.objects.get(
                                pk=product['fields']['category']),
                            price=product['fields']['price'],
                            created_at=product['fields']['created_at'],
                            updated_at=product['fields']['updated_at'],
                            )
                )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
