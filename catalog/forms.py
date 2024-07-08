import json

from django.forms import ModelForm, forms

from catalog.models import Product, Version


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name_product(self):
        cleaned_data = self.cleaned_data.get("name_product")

        with open("forbidden_words.json", "rt", encoding="utf-8") as file:
            forbidden_words = json.load(file)

        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError("Недопустимое слово")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get("description")

        with open("forbidden_words.json", "rt", encoding="utf-8") as file:
            forbidden_words = json.load(file)

        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError("Недопустимое слово")
        return cleaned_data


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
