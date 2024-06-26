from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductsListView, ContactsView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductsListView.as_view(), name="base"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="products_detail"),
]
