from config.settings import CACHES_ENABLED
from catalog.models import Product, Category
from django.core.cache import cache
from django.conf import settings


def get_products_from_cache():
    """
    Получает данные о продукте из кеша, если кеш пуст, получает данные из БД
    """
    # Если кеш выключен, получаем данные из БД вручную
    if not CACHES_ENABLED:
        return Product.objects.all()

    key = "products_list"

    # Получаем данные из кеша
    products = cache.get(key)

    # Если данные в кеше не найдены, получаем данные из БД и добавляем их в кеш
    if products is None:
        products = Product.objects.all()
        cache.set(key, products)

    return products


def get_category_list_cache():
    """
    Получает данные о продукте из кеша, если кеш пуст, получает данные из БД
    """

    if settings.CACHES_ENABLED:
        key = "category_list"
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()
    return category_list
