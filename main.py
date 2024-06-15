import google.generativeai as genai
import os
from jinja2 import FileSystemLoader, Environment
from helpers import *

genai.configure(api_key=os.environ['GEMINI_API_KEY'])

url = 'https://politicalviolenceataglance.org/2018/02/09/how-civil-wars-end/'
tag = "Most wars today end in negotiation"
year = "18"
last_name = "Howard"
paragraphs = get_paragraphs(url)
site_content = " ".join(paragraphs)

prompt = f"Given the following text, directly quote any and all relevant information from the text that supports the argument {tag}:" \
         f"{site_content}" \
         f"Do not paraphrase anything" \
         f"Limit your response to three quotes or less" \

model = genai.GenerativeModel()
response = model.generate_content(prompt)
print(response)
response = response.text
print(response)

quotes = get_quote_from_response(response)
context = get_context(quotes, paragraphs)
environment = Environment(loader=FileSystemLoader("templates/"))

with open('card.html', 'w') as card:
    card.write(get_card_html(environment, tag, last_name, year, url, context, quotes))

with open('card.css', 'w') as card:
    card.write(get_card_css(environment))