from requests import get
from bs4 import BeautifulSoup
from datetime import date
import json


def get_paragraphs(url):
    content = []
    r = get(url)
    r.encoding = 'utf-8'
    paras = BeautifulSoup(r.text, 'html.parser').findAll('p')
    for para in paras:
        content.append(para.get_text())
    return content


# def get_mla_citation(url):
#     r = get(url)
#     soup = BeautifulSoup(r.text, 'html.parser')
#
#     title = soup.title.string.strip() if soup.title else ''
#     data = json.loads(soup.select_one('[type="application/ld+json"]').contents[0])
#
#     # uncomment this to print all LD+JSON data:
#     # print(json.dumps(data, indent=4))
#
#     first_name, last_name = (data["author"]["name"])).split()
#     publication_date = ''
#     date_acessed = date.today()
#
#     # Example of a simple MLA citation format
#     mla_citation = f'{first_name} {last_name}. "{title}." {publication_date}, {url}.'
#
#     return mla_citation, last_name

