import random
import time
import re
from requests_html import HTMLSession()


#for i in range(1, 12):
 #   ran = random.randint(2, 6)
  #  print(ran)
   # time.sleep(ran)

url = "https://www.amazon.de/blackfriday?ref_=nav_cs_td_bf_dt_cr"

session = HTMLSession()

r = session.get(url)

r.html.render(sleep=1, keep_page=True, scrolldown=2)


str = "1-40 von 796 Ergebnissen für"
num = re.findall(r'[0-9]+', str)
print(num)

if num[2] <= 40:
    pages = 1
elif num[2] == num[1]:
    pages = 1
elif num[2] % 40 == 0:
    pages = num[2] / 40
elif num[2] > 40:
    pages = (num[2] // 40) + 1
