# parser.py
import requests
import os, json, re
from bs4 import BeautifulSoup

# Location of parser.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# HTTP GET Request
request =  requests.get('https://github.com/alstn2468?tab=repositories')

# GET HTML Source
html = request.text

# Use BeautifulSoup, From HTML Source to Python Object
# First Parameter is HTML Source, Second Parameter is the parser to be used
soup = BeautifulSoup(html, 'html.parser')

# HTML element using CSS Selector
repo_titles = soup.select('#user-repositories-list > ul > li > div.d-inline-block.mb-1 > h3 > a')

data = {}

# repo_titles is list object
for title in repo_titles:
    data[''.join((title.text).split())] = 'https://www.github.com' + title.get('href')

# Saving the Crolling Data to a JSON File
with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file, indent = '\t')

# GET HTTP Header
header = request.headers

# GET HTTP Status ( 200 : normal )
status = request.status_code

# Check HTTP ( TRUE / FALSE )
is_HTTP_OK = request.ok
