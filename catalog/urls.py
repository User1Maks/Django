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
                           BlogDeleteView
                           )

app_name = CatalogConfig.name

urlpatterns = [

    path("", ProductsListView.as_view(), name="product_list"),
    path("products/create/", ProductCreateView.as_view(),
         name="product_create"),
    path("product/<int:pk>/update", ProductUpdateView.as_view(),
         name="product_update"),
    path("products/<int:pk>/", ProductDetailView.as_view(),
         name="product_detail"),
    path("product/<int:pk>/delete", ProductDeleteView.as_view(),
         name="product_delete"),

    path("contacts/", ContactsView.as_view(), name="contacts"),

    path("blog/list/", BlogListView.as_view(), name="blog_base"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog/create", BlogCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/update", BlogUpdateView.as_view(), name="blog_update"),
    path("blog/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
]
