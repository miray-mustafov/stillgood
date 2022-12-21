from django import forms

from project_1.items.models import Item


class ItemAddForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('user', 'date_added', 'is_favourite')

        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': '...',
                'cols': 42,
                'rows': 5,
            }),
        }


class ItemEditForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('user', 'date_added')

        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': '...',
                'cols': 42,
                'rows': 5,
            }),
        }
