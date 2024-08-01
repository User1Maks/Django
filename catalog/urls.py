from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (ProductsListView,
                           ProductCreateView,
                           ProductUpdateView,
                           ProductDeleteView,
                           ContactsView,
                           ProductDetailView,
                           BlogCreateView,
                           BlogListView,
                           BlogUpdateView,
                           BlogDetailView,
                           BlogDeleteView,
                           CategoryListView
                           )
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    # Продукты
    # Первый способ кеширования для списка продуктов реализован в services.py
    path("", ProductsListView.as_view(), name="product_list"),
    path("products/create/", ProductCreateView.as_view(),
         name="product_create"),
    path("product/<int:pk>/update", ProductUpdateView.as_view(),
         name="product_update"),
    # Второй способ кеширования реализован через cache_page в urls.py
    path("products/<int:pk>/", cache_page(120)(ProductDetailView.as_view()),
         name="product_detail"),
    path("product/<int:pk>/delete", ProductDeleteView.as_view(),
         name="product_delete"),

    # Контакты
    path("contacts/", ContactsView.as_view(), name="contacts"),

    # Блог
    path("blog/list/", BlogListView.as_view(), name="blog_base"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog/create", BlogCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/update", BlogUpdateView.as_view(), name="blog_update"),
    path("blog/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),

    # Категории
    path("category/list", CategoryListView.as_view(), name="category_list"),
]
