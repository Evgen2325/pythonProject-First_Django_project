from .models import Bills
from django.forms import ModelForm, TextInput, DateTimeInput


class BillsForm(ModelForm):
    class Meta:
        model = Bills
        fields = ['title', 'price', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),

        }