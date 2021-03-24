from requests_html import HTMLSession
import requests
import time
import random
import re

compl_url_list = []
starting_url = "https://www.amazon.de/blackfriday?ref_=nav_cs_td_bf_dt_cr"

#print(subtoptic_url_list)
def All_urls(url_input=starting_url):
    url = url_input

    session = HTMLSession()

    r = session.get(url)

    r.html.render(sleep=1, keep_page=True, scrolldown=2)

    url_data = r.html.find(".a-declarative")

    subtoptic_url_list = []
    subtopic_par = []

    for i in url_data:
        gbfilter = i.attrs.get("data-gbfilter-checkbox")
        if gbfilter == None:
            continue
        else:
            spliited_filter = gbfilter.split("\"")
            url_par = spliited_filter[7]

            amz_url = f'https://www.amazon.de/blackfriday/ref=gbps_ftr___page_1?gb_f_GB-SUPPLE=enforcedCategories:3167641517801%252C{url_par},dealTypes:DEAL_OF_THE_DAY%252CBEST_DEAL%252CLIGHTNING_DEAL,page:1,sortOrder:BY_SCORE,dealsPerPage:30&ie=UTF8'
            #subtoptic_url_list.append(amz_url)
            req = requests.get(amz_url).status_code
            if req == 200 or req == 503:
                subtopic_par.append(url_par)
            #print(req.status_code)
            #print(amz_url)
            time.sleep(random.randint(2, 6))



    for subtopic_parameter in subtopic_par:
        url = f'https://www.amazon.de/blackfriday/ref=gbps_ftr___page_1?gb_f_GB-SUPPLE=enforcedCategories:3167641517801%252C{subtopic_parameter},dealTypes:DEAL_OF_THE_DAY%252CBEST_DEAL%252CLIGHTNING_DEAL,page:1,sortOrder:BY_SCORE,dealsPerPage:30&ie=UTF8'

        status_header1 = requests.get(url).status_code
        if status_header1 != 200 and status_header1 != 503:
            continue

        session = HTMLSession()

        r = session.get(url)

        r.html.render(sleep=1, keep_page=True, scrolldown=2)

        str = r.html.find(".a-pagination")

        list = []
        for i in str:
            texte = i.text
            list.append(texte)

        if list[0] == [] or list == None:
            continue
        string = list[0]

        num = re.findall(r'[0-9]+', string)
        number_of_pages = int(num[3])
        if type(number_of_pages) is not int:
            continue


        for num_of_pages in number_of_pages:
            compl_url = f'https://www.amazon.de/blackfriday/ref=gbps_ftr___page_{num_of_pages}?gb_f_GB-SUPPLE=enforcedCategories:3167641517801%252C{subtopic_parameter},dealTypes:DEAL_OF_THE_DAY%252CBEST_DEAL%252CLIGHTNING_DEAL,page:{num_of_pages},sortOrder:BY_SCORE,dealsPerPage:30&ie=UTF8'
            status_header2 = requests.get(url).status_code
            if status_header2 != 200 and status_header2 != 503:
                continue
            compl_url_list.append(compl_url)

    return compl_url_list


print(All_urls())
