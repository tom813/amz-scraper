import requests
from bs4 import BeautifulSoup


url = 'https://www.amazon.de/primeday/2/ref=gbpp_itr___COMPUTER?gb_f_GB-SUPPLE=enforcedCategories:301927%252C340843031&gb_ttl_GB-SUPPLE=Computer%2520und%2520Zubeh%C3%B6r%2520Angebote&ie=UTF8'


response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

next_pages = soup.find_all(class_="priceBlock")

for next_page in next_pages:
    print(next_page.text)


