import requests
import codecs
from bs4 import BeautifulSoup as BS
from random import randint

__all__ = ('habr_vacancy', 'head_hunter')


headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
]


urlHabr = 'https://career.habr.com/vacancies?q=Python&type=suitable'


def replace_word(url):
    end_point = url.find('?query')
    return url[0:end_point]



def habr_vacancy(url):
    resp = requests.get(urlHabr, headers=headers[randint(0, 2)])
    jobs = []
    errors = []
    domain = 'https://career.habr.com'
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('ul', attrs={'class': 'card-list--appearance-within-section'})
        if main_div:
            div_lst = main_div.find_all('li', attrs={'class': 'card-list__item'})
            for item in div_lst:
                title = item.find('div', attrs={'class': 'vacancy-card__title'})
                href = title.a['href']
                content = item.find('div', attrs={'class': 'vacancy-card__meta'})
                requirement = item.find('div', attrs={'class': 'vacancy-card__skills'})
                company = content.find('a')
                jobs.append({'title': title.text, 'url': domain + href, 'description': content.text,
                             'requirement': requirement.text, 'company_name': company.text})
        else:
            errors.append({'url': urlHabr, 'title': 'Div does not exist'})
    else:
        errors.append({'url': urlHabr, 'title': 'Page don\'t response'})
    return jobs, errors
    

def head_hunter(url):
    resp = requests.get(url, headers=headers[randint(0, 2)])
    jobs = []
    errors = []
    domain = 'https://hh.ru/'
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', attrs={'class': 'vacancy-serp'})
        if main_div:
            div_lst = main_div.find_all('div', attrs={'class': 'vacancy-serp-item'})
            for item in div_lst:
                title = item.find('a', attrs={'class': 'HH-LinkModifier'})
                href = replace_word(title['href'])
                content = item.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'})
                requirement = item.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'})
                company = item.find('a', attrs={'class': 'bloko-link_secondary'})
                jobs.append({'title': title.text, 'url': href, 'description': content.text,
                             'requirement': requirement.text, 'company_name': company.text})
        else:
            errors.append({'url': url, 'title': 'Div does not exist'})
    else:
        errors.append({'url': url, 'title': 'Page don\'t response'})
    return jobs, errors
    
    
if __name__ == '__main__':
    urlHabr = 'https://career.habr.com/vacancies?q=Python&type=suitable'
    url = 'https://ufa.hh.ru/search/vacancy?area=1&clusters=true&enable_snippets=true&text=python&experience=noExperience&from=cluster_experience&showClusters=true'
    jobs, errors = habr_vacancy(urlHabr)
    h = codecs.open('../work.html', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()


