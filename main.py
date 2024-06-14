import google.generativeai as genai
import os
from scrapers import *

genai.configure(api_key=os.environ['GEMINI_API_KEY'])

url = 'https://www.geopoliticalmonitor.com/russias-tough-talk-on-arctic-sovereignty-must-be-taken-seriously/'
tag = "Russia and NATO tensions are growing"
paragraphs = get_paragraphs(url)
site_content = " ".join(paragraphs)

prompt = f"Given the following text, directly quote any and all relevant information from the text that supports the argument {tag}:" \
         f"{site_content}" \
         f"Do not paraphrase anything" \
         f"Limit your response to three quotes or less" \

model = genai.GenerativeModel()
response = model.generate_content(prompt)

