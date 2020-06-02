from django.shortcuts import render
from .models import Vacancy
from .forms import SearchForm


def index_view(request):
    form = SearchForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    query = []
    if language or city:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language
            
        query = Vacancy.objects.filter(**_filter)
    return render(request, 'base/index.html', {'object_list': query, 'form': form})
