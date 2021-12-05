from .models import Rate
from django.forms import ModelForm, TextInput, Textarea


class RateForm(ModelForm):
    class Meta:
        model = Rate
        fields = ['name', 'description']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }
