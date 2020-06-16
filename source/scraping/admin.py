from django.contrib import admin
from .models import City, LanguageProgramming, Vacancy, Error

admin.site.register(City)
admin.site.register(LanguageProgramming)
admin.site.register(Vacancy)
admin.site.register(Error)

