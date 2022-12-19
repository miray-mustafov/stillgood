from django import forms

from project_1.core.my_enums import Conditions
from project_1.items.models import Item


class ItemBaseForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('user',)


class ItemDetailsForm(ItemBaseForm):
    pass


class ItemAddForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('user', 'date_added')
        labels = {
            'title': 'Title:',
            'is_new': 'new:',
        }

        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': '...',
                'cols': 42,
                'rows': 5,
            }),
            'condition': forms.RadioSelect(choices=Conditions.choices())
        }


class ItemEditForm(ItemBaseForm):
    pass


class ItemDeleteForm(ItemBaseForm):
    pass
