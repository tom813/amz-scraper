import requests
from bs4 import BeautifulSoup
from url_list import full_url_list

url = 'https://www.amazon.de/deal/44a5bad0/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#title = soup.find('title')
savings = soup.find_all(class_="octopus-widget-price-saving-percentage")
title = soup.find_all(class_="a-size-base")
price_euro = soup.find_all(class_="a-price-whole")
price_cent = soup.find_all(class_="a-price-fraction")


ult_list = []

for loop in range(0, len(savings)):
    saving_filtered = savings[loop].text
    while ' ' in saving_filtered:
        saving_filtered = saving_filtered.replace(" ", "").replace("(", "").replace(")", "")

    while '\n' in saving_filtered:
        saving_filtered = saving_filtered.replace("\n", "")

    title_filtered = title[loop].text
    while ' ' in title_filtered:
        title_filtered = title_filtered.replace(" ", "")

    while '\n' in title_filtered:
        title_filtered = title_filtered.replace("\n", "")


    price_euro_filtered = price_euro[loop].text
    price_cent_filtered = price_cent[loop].text
    price_sum = f'{price_euro_filtered}{price_cent_filtered}'
    #print(saving_filtered)
    #print(title_filtered)
    #print(price_sum)
    dict = {
        "Prozent": saving_filtered,
        "Titel": title_filtered,
        "Preis": price_sum
    }
    ult_list.append(dict)


print(ult_list)

