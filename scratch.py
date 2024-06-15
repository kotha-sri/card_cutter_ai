from helpers import *
from jinja2 import FileSystemLoader, Environment
import json

response = "- \"Russia indeed thinks that it has a lot at stake.\"" \
           "- \"Russia will 'step up' (Russian: активизации) the delineating of these borders in a region it identifies as the second most important after the countries of central Asia and eastern Europe, and what it calls the 'near abroad.'\"" \
           "- \"The Maritime Doctrine describes the Arctic Ocean as the only 'vital' ocean to national interests, with its socio-economic development a 'decisive condition' for future prosperity.\""
quotes = get_quote_from_response(response)
url = 'https://www.geopoliticalmonitor.com/russias-tough-talk-on-arctic-sovereignty-must-be-taken-seriously/'
paragraphs = get_paragraphs(url)
tag = "Russia and NATO tensions are growing"
last_name = "Dalziel"
year = "24"
context = get_context(quotes, paragraphs)

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

with open('card.html', 'w') as card:
    card.write(card_html)
