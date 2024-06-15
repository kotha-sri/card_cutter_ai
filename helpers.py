import re
from scrapers import *
from anyascii import anyascii
import json

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
    print(paragraphs)
    return (first-1 if first != 0 else first, last+1 if last != len(paragraphs) else last), paragraphs


def format_content(paragraphs, quotes, context):
    content = " ".join(paragraphs[context[0]:context[1]])
    for quote in quotes:
        content = content.replace(quote, f'<span class="read">{quote}</span>')
    return content

def get_card_css(environment):
    card_css_template = environment.get_template('card_template.css')
    with open('config.json', 'r') as config:
        config_dict = json.loads(config.read())
    card_css = card_css_template.render(
        body_background_color=config_dict['body_background_color'],
        font_family=config_dict['font_family'],
        tag_font_size=config_dict['tag_font_size'],
        tag_is_bolded="bold" if config_dict['tag_is_bolded'] == True else "none",
        citation_font_size=config_dict['citation_font_size'],
        content_font_size=config_dict['content_font_size'],
        read_font_size=config_dict['read_font_size'],
        read_is_bolded="bold" if config_dict['read_is_bolded'] == True else "none",
        read_is_underlined="underline" if config_dict['read_is_underlined'] == True else "none",
        read_highlight_color=config_dict['read_highlight_color']
    )
    return card_css

# TODO change url param to citation
def get_card_html(environment, tag, last_name, year, url, context, quotes):
    card_html_template = environment.get_template('card_template.html')
    card_html = card_html_template.render(
        tag=tag,
        last_name=last_name,
        year=year,
        citation=url,
        card_body=anyascii(format_content(context[1], quotes, context[0]))
    )
    return card_html