from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (ProductsListView,
                           ContactsView,
                           ProductDetailView,
                           BlogCreateView,
                           BlogListView,
                           BlogUpdateView,
                           BlogDetailView,
                           BlogDeleteView
                           )

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductsListView.as_view(), name="base"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products/<int:pk>/", ProductDetailView.as_view(),
         name="products_detail"),
    path("blog/list/", BlogListView.as_view(), name="blog_base"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog/create", BlogCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/update", BlogUpdateView.as_view(), name="blog_update"),
    path("blog/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
]
