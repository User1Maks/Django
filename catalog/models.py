from django.db import models

from users.models import User, NULLABLE


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
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Категория",
        related_name="products",
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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name="Владелец", related_name="products")

    is_published = models.BooleanField(
        default=True, verbose_name="Опубликовано",
        help_text="Опубликовать продукт"
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
        # Для определения прав доступа
        permissions = [
            # может отменять публикацию продукта
            ("can_edit_is_published", "Can edit is published"),
            # может менять описание любого продукта
            ("can_edit_description", "Can edit description"),
            # может менять категорию любого продукта
            ("can_edit_category", "Can edit category"),

        ]


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="versions",
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Продукты",
    )
    version_number = models.PositiveIntegerField(
        verbose_name="Номер версии",
        help_text="Введите номер версии продукта",
        default=1,
    )
    name_version = models.CharField(
        max_length=100,
        verbose_name="Название версии",
        help_text="Введите название версии продукта",
        **NULLABLE
    )
    current_version = models.BooleanField(
        default=True,
        verbose_name="Текущая версия",
        help_text="Отметьте, является ли текущей версией продукта актуальной",
    )

    def __str__(self):
        return f"{self.version_number} - {self.name_version}"

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продуктов"


class Blog(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Заголовок",
        help_text="Введите заголовок статьи"
    )
    slug = models.CharField(max_length=200, verbose_name="slug")
    content = models.TextField(verbose_name="Содержание")
    preview_image = models.ImageField(
        upload_to="blog/image",
        verbose_name="Изображение",
        **NULLABLE,
        help_text="Загрузите изображение статьи",
    )
    created_at = models.DateField(
        auto_now_add=True,
        editable=False,
        verbose_name="Дата создания (записи в БД)",
        null=True,
    )
    is_published = models.BooleanField(
        default=True, verbose_name="Опубликовано",
        help_text="Опубликовать статью"
    )
    view_counter = models.PositiveIntegerField(
        default=0, editable=False, verbose_name="Количество просмотров"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
