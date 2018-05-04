import requests
from bs4 import BeautifulSoup
import re

url = "https://rozetka.com.ua/msi_ge72mvr7rg_075xua/p31373959/"
tag_name = 'meta'
query = {"itemprop": "price"}

request = requests.get(url)
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find(tag_name, query)
string_price = element.text.strip()

pattern = re.compile("(\d+)\.(\d+)")  #  [\d+].?[\d+]  (\d+)
match = pattern.search(string_price)

print(float(match.group()))