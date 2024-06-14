import re
from scrapers import *
from anyascii import anyascii

response = "- \"Russia indeed thinks that it has a lot at stake.\"" \
           "- \"Russia will 'step up' (Russian: активизации) the delineating of these borders in a region it identifies as the second most important after the countries of central Asia and eastern Europe, and what it calls the 'near abroad.'\"" \
           "- \"The Maritime Doctrine describes the Arctic Ocean as the only 'vital' ocean to national interests, with its socio-economic development a 'decisive condition' for future prosperity.\""

paragraphs = get_paragraphs('https://www.geopoliticalmonitor.com/russias-tough-talk-on-arctic-sovereignty-must-be-taken-seriously/')

def get_quote_from_response(response):
    return re.findall('"(.*?)"', response)

def get_context(quotes, paragraphs):
    for i in range(len(quotes)):
        quotes[i] = quotes[i].replace("'", '\"')
    first = 10000
    last = 0
    for i in range(len(paragraphs)):
        for quote in quotes:
            if quote in paragraphs[i] or quote in anyascii(paragraphs[i]):
                if i < first:
                    first = i
                if i > last:
                    last = i
                if quote not in paragraphs[i]:
                    paragraphs[i] = anyascii(paragraphs[i])
    return (first-1 if first != 0 else first, last+1 if last != len(paragraphs) else last), paragraphs

def format_tagline(tag, author, year):
    return f'\t\t<p style="font-size:13pt; font-weight:bold; padding:0; margin:0;">{tag}</p>\n' \
           f'\t\t<p style="font-size:13pt; font-weight:bold; padding:0; margin:0;">{author} {year}\'</p>\n'

def format_citation(citation):
    return f'\t\t<p style="font-size:9pt; padding-bottom:9pt; margin:0;">{citation}</p>\n'

def format_content(paragraphs, quotes, context):
    content = " ".join(paragraphs[context[0]:context[1]])
    for quote in quotes:
        content = content.replace(quote, f'<span style="font-size:11pt; background-color:#00FFFF; font-weight:bold; text-decoration:underline;">{quote}</span>')
    return content