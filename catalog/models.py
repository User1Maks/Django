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
        return f"{self.name_category}"

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
        upload_to="products/image",
        **NULLABLE,
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта"
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        **NULLABLE, verbose_name="Категория",
        related_name="products"
    )
    price = models.FloatField(verbose_name="Цена за покупку")
    created_at = models.DateField(
        auto_now_add=True,
        editable=False,
        verbose_name="Дата создания (записи в БД)",
        null=True,
    )
    updated_at = models.DateField(
        auto_now=True,
        editable=False,
        verbose_name="Дата последнего изменения (записи в БД)",
        null=True,
    )

    def __str__(self):
        return f"{self.name_product}"

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


class Blog(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок статьи"
    )
    slug = models.CharField(max_length=200,
                            verbose_name="slug")
    content = models.TextField(verbose_name="Содержание")
    preview_image = models.ImageField(upload_to="blog/image",
                                      verbose_name="Изображение",
                                      **NULLABLE,
                                      help_text="Загрузите изображение статьи")
    created_at = models.DateField(
        auto_now_add=True,
        editable=False,
        verbose_name="Дата создания (записи в БД)",
        null=True
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
        help_text="Опубликовать статью"
    )
    view_counter = models.PositiveIntegerField(
        default=0,
        editable=False,
        verbose_name="Количество просмотров"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
