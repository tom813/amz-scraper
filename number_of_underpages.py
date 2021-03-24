from requests_html import HTMLSession
import re

url = "https://www.amazon.de/blackfriday/ref=gbps_ftr___page_2?gb_f_GB-SUPPLE=dealTypes:DEAL_OF_THE_DAY%252CBEST_DEAL%252CLIGHTNING_DEAL,page:2,sortOrder:BY_SCORE,enforcedCategories:84230031,dealsPerPage:60&ie=UTF8"

session = HTMLSession()

r = session.get(url)

r.html.render(sleep=1, keep_page=True, scrolldown=2)


str = r.html.find(".a-pagination")

list = []
for i in str:
    texte = i.text
    list.append(texte)

string = list[0]

num = re.findall(r'[0-9]+', string)
print(int(num[3]))


