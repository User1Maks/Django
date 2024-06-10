from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name_category = models.CharField(
        max_length=50, verbose_name="Категория",
        help_text="Введите название категории"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание товара"
    )

    def __str__(self):
        return f"{self.name_category}\n" f"{self.description}\n"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name_product = models.CharField(
        max_length=100, verbose_name="Товар",
        help_text="Введите наименование товара"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание товара", **NULLABLE
    )
    image = models.ImageField(
        upload_to="products/", **NULLABLE, help_text="Загрузите фото продукта"
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 **NULLABLE, related_name='products')
    price = models.FloatField(verbose_name="Цена за покупку")
    created_at = models.DateField(
        auto_now_add=True,
        editable=False,
        verbose_name="Дата создания (записи в БД)",
        null=True)
    updated_at = models.DateField(
        auto_now=True,
        editable=False,
        verbose_name="Дата последнего изменения (записи в БД)",
        null=True
    )

    def __str__(self):
        return f"{self.name_product}\n" f"{self.description}\n"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

        # Сортировка
        ordering = [
            "name_product",
            "category",
            "price",
            "created_at",
            "updated_at",
        ]
