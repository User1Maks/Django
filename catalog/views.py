from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(requests):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(requests, "products_list.html", context)


def contacts(requests):
    if requests.method == "POST":
        name = requests.POST.get("name")
        phone = requests.POST.get("phone")
        message = requests.POST.get("message")
        print(f"{name}: {phone}\n {message}")

    return render(requests, "contacts.html")


def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product
    }
    return render(request, 'products_detail.html', context)
