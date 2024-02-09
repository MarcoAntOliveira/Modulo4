import requests
from bs4 import BeautifulSoup 
import re

url = 'http://localhost:8000/'
response = requests.get(url)
raw_html= response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

#print(parsed_html.text)
top_jobs_heading= parsed_html.select_one('#intro > div > div > article > h2')
print(top_jobs_heading.text)

if top_jobs_heading is not None:
    article = top_jobs_heading.parent
    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ',p.text).strip())
