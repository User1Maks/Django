from django.shortcuts import render

from catalog.models import Product


def home(requests):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(requests, "home.html", context)


# def home(requests):
#     return render(requests, "home.html")


def contacts(requests):
    if requests.method == "POST":
        name = requests.POST.get("name")
        phone = requests.POST.get("phone")
        message = requests.POST.get("message")
        print(f"{name}: {phone}\n {message}")

    return render(requests, "contacts.html")
