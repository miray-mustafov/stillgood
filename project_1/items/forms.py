from django import forms

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

        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': '...',
                'cols': 42,
                'rows': 5,
            }),
        }


class ItemEditForm(ItemBaseForm):
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


class ItemDeleteForm(ItemBaseForm):
    pass
