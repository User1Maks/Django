from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView, DetailView, View


class ProductsListView(ListView):
    model = Product

    # app_name/<model_name>_<action>
    # catalog/product_list.html


class ProductDetailView(DetailView):
    model = Product


class ContactsView(View):
    def get(self, requests):
        return render(requests, "catalog/contacts.html")

# def products_list(requests):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list
#     }
#     return render(requests, "products_list.html", context)


# def products_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         "product": product
#     }
#     return render(request, 'product_detail.html', context)

# def contacts(requests):
#     if requests.method == "POST":
#         name = requests.POST.get("name")
#         phone = requests.POST.get("phone")
#         message = requests.POST.get("message")
#         print(f"{name}: {phone}\n {message}")
#
#     return render(requests, "catalog/contacts.html")
