from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(max_length=50, empty_value='@', )
    categ_id = forms.IntegerField()
