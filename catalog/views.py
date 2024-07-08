from django.shortcuts import render
from django.forms import inlineformset_factory
from catalog.forms import ProductForm, VersionForm
from django.core.exceptions import ObjectDoesNotExist
from catalog.models import Product, Blog, Version
from django.views.generic import (
    ListView,
    DetailView,
    View,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify


class GetContextMixin:
    def get_context_data(self, **kwargs):
        """
        Метод добавляет поле 'current_version' в контекст шаблона.
        :param kwargs:
        :return:
        """
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm,
                                               extra=1)
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        """Метод сохраняет данные формы по "formset" """
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )


class ProductsListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for obj in context['object_list']:
            try:

                if len(obj.versions.filter(current_version=True)) > 1:
                    obj.active_version = obj.versions.filter(current_version=True).last()
                else:
                    obj.active_version = obj.versions.get(current_version=True)
            except ObjectDoesNotExist:
                obj.active_version = "Версия продукта не указана"
        return context

    # app_name/<model_name>_<action>
    # catalog/product_list.html


# def products_list(requests):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list
#     }
#     return render(requests, "products_list.html", context)


class ProductCreateView(GetContextMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(GetContextMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class ProductDetailView(DetailView):
    model = Product


# def products_detail(request, pk):


#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         "product": product
#     }
#     return render(request, 'product_detail.html', context)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


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
