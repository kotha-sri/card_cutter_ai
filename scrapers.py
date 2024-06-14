from requests import get
from bs4 import BeautifulSoup

def get_paragraphs(url):
    content = []
    r = get(url)
    r.encoding = 'utf-8'
    paras = BeautifulSoup(r.text, 'html.parser').findAll('p')
    for para in paras:
        content.append(para.get_text())
    return content

def get_citation(url):
    pass

