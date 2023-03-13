from django import forms
from .models import Product
from .models.product import CategoryChoice


class ProductForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CategoryChoice.choices, label="Категория")
    image = forms.URLField(max_length=2000, required=False, label="Фото товара")
    remains = forms.IntegerField(min_value=0, required=True, label="Остаток")
    price = forms.DecimalField(min_value=0, required=True, max_digits=7, decimal_places=2, label="Стоимость")

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'remains', 'price']
        labels = {
            'name': 'Наименование товара',
            'description': 'Описание товара',
            'image': 'Фото товара',
            'remains': 'Остаток',
            'price': 'Стоимость'
        }

    def clean_remains(self):
        remains = self.cleaned_data['remains']
        if remains < 0:
            raise forms.ValidationError("Остаток должен быть положительным числом")
        return remains

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("Стоимость должна быть положительным числом")
        return price
