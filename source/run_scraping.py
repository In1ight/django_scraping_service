import codecs

import os, sys

from django.db import DatabaseError

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'scraping_service.settings'

import django
django.setup()

from scraping.parsers import *

from scraping.models import Vacancy, City, LanguageProgramming

parsers = (
           (habr_vacancy, 'https://career.habr.com/vacancies?q=Python&type=suitable'),
           (head_hunter, 'https://ufa.hh.ru/search/vacancy?area=1&clusters=true&enable_snippets=true&text=python&experience=noExperience&from=cluster_experience&showClusters=false')
)
city = City.objects.filter(slug='moskva').first()
language = LanguageProgramming.objects.filter(slug='python').first()

jobs, errors = [], []
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e
    a = 1
    
for item in jobs:
    v = Vacancy(**item, city=city, language=language)
    try:
        v.save()
    except DatabaseError:
        pass
    
# h = codecs.open('../work.html', 'w', 'utf-8')
# h.write(str(jobs))
# h.close()