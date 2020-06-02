from django import forms
from .models import City, LanguageProgramming


class SearchForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(),
                                  to_field_name='slug', required=False,
                                  widget=forms.Select(attrs={'class': 'form-control'}),
                                  label='Город')
    language = forms.ModelChoiceField(queryset=LanguageProgramming.objects.all(),
                                      to_field_name='slug', required=False,
                                      widget=forms.Select(attrs={'class': 'form-control'}),
                                      label='Специальность')