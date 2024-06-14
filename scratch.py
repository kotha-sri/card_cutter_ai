from helpers import *
from jinja2 import Template, FileSystemLoader, Environment

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

# TODO: use the methods in helper to write to 'card.html' a div of the card with a copy button next to it

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template('card_template.html')
card_content = template.render(
    tag=tag,
    last_name=last_name,
    year=year,
    citation=url,
    card_body=anyascii(format_content(context[1], quotes, context[0]))
)

with open('card.html', 'w') as card:
    card.write(card_content)

