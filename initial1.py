import requests

from bs4 import BeautifulSoup

response = requests.get('https://www.kaufda.de/webapp/?lat=51.8441&lng=10.7767&zip=38855')
soup = BeautifulSoup(response.content, 'html.parser')

#print(soup.prettify())

content_div = soup.find_all('div', class_=['card', 'card--brochure', 'slider-preventClick']);
if content_div:
  print('found')
else:
    print("No article content found.")