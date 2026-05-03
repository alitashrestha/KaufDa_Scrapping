import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

element_list = []
# Use a proper Service object
service = Service(ChromeDriverManager().install())


# Initialize driver properly
driver = webdriver.Chrome(service=service)
url = f"/webapp/viewer/a1ee7f68-722c-413d-bfbf-e322df56f124?pageType=DE-P-Global_Startpage&sourceType=PORTAL_STARTPAGE&lat=51.8441&lng=10.7767"
driver.get(url)
time.sleep(2)  # Optional wait to ensure page loads

soup = BeautifulSoup(driver.page_source, 'html.parser')


content_div = soup.find_all('div', class_=['card', 'card--brochure', 'slider-preventClick']);

if content_div:
    # for element in content_div:
    element = content_div[0]
     #   print(element,"\n")
    links = element.find_all('a')
    for link in links:
          element_list.append(link.get('href'))
else:
    print("No article content found.")
    
print(element_list)
# cards = driver.find_elements(By.CLASS_NAME, "ad-unit-display");

# if cards:
#     for para in cards:
#         print(para)
# else:
#     print("No article content found.")
