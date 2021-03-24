import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.de/deal/782c6c76/ref=gbps_rlm___782c6c76?smid=A3DLCFJMTRPCSY'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

#links = soup.find_all('a', href=True)
links = soup.find_all(class_="a-link-normal")

for link in links:
    print(link)
    print('------')
    print(link['href'])
    print('---------------------------------')


img_sections = soup.find_all(class_="octopus-dlp-image-shield")

#for img_section in img_sections:
 #   print(img_section.text)