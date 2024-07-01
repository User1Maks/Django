from django.shortcuts import render
from catalog.models import Product, Blog
from django.views.generic import (ListView,
                                  DetailView,
                                  View,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify


class ProductsListView(ListView):
    model = Product

    # app_name/<model_name>_<action>
    # catalog/product_list.html


# def products_list(requests):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list
#     }
#     return render(requests, "products_list.html", context)

class ProductDetailView(DetailView):
    model = Product


# def products_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         "product": product
#     }
#     return render(request, 'product_detail.html', context)


class ContactsView(View):
    def get(self, requests):
        return render(requests, "catalog/contacts.html")


# def contacts(requests):
#     if requests.method == "POST":
#         name = requests.POST.get("name")
#         phone = requests.POST.get("phone")
#         message = requests.POST.get("message")
#         print(f"{name}: {phone}\n {message}")
#
#     return render(requests, "catalog/contacts.html")


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "preview_image", "is_published")
    success_url = reverse_lazy("catalog:blog_base")

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "preview_image", "is_published")
    success_url = reverse_lazy("catalog:blog_base")

    def get_success_url(self):
        return reverse("catalog:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("catalog:blog_base")
