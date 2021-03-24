from requests_html import HTMLSession

session = HTMLSession()

#url = 'https://www.amazon.de/primeday/2/ref=gbpp_itr___COMPUTER?gb_f_GB-SUPPLE=enforcedCategories:301927%252C340843031&gb_ttl_GB-SUPPLE=Computer%2520und%2520Zubeh%C3%B6r%2520Angebote&ie=UTF8&nocache=1602609356879'

url_input_list = [
    'https://www.amazon.de/primeday/2/ref=gbpp_itr___TOYS?gb_f_GB-SUPPLE=enforcedCategories:12950651&gb_ttl_GB-SUPPLE=Spielzeug%2520Angebote&ie=UTF8',
    'https://www.amazon.de/primeday/2/ref=gbpp_itr___HOME?gb_f_GB-SUPPLE=enforcedCategories:3167641%252C3517801&gb_ttl_GB-SUPPLE=K%C3%BCche%2520Haushalt%2520und%2520M%C3%B6bel%2520Angebote&ie=UTF8',
    'https://www.amazon.de/primeday/2/ref=gbpp_itr___MOBPHONE?gb_f_GB-SUPPLE=enforcedCategories:1384526031&gb_ttl_GB-SUPPLE=Smartphone%2520Angebote&ie=UTF8',
    'https://www.amazon.de/primeday/2/ref=gbpp_itr___HPC?gb_f_GB-SUPPLE=enforcedCategories:64187031&gb_ttl_GB-SUPPLE=Drogerie%2520und%2520K%C3%B6rperpflege%2520Angebote&ie=UTF8',
    'https://www.amazon.de/primeday/2/ref=gbpp_itr___COMPUTER?gb_f_GB-SUPPLE=enforcedCategories:301927%252C340843031&gb_ttl_GB-SUPPLE=Computer%2520und%2520Zubeh%C3%B6r%2520Angebote&ie=UTF8',
    'https://www.amazon.de/primeday/2/ref=gbpp_itr___CAMERA?gb_f_GB-SUPPLE=enforcedCategories:571860&gb_ttl_GB-SUPPLE=Kamera%2520Angebote&ie=UTF8',
    #'https://www.amazon.de/gcx/Geschenke-f%C3%BCr-Erwachsene/gfhz/ref=gbpp_itr___GIFTGUID?ie=UTF8&isLimitedTimeOffer=true&scrollState=eyJpdGVtSW5kZXgiOjAsInNjcm9sbE9mZnNldCI6NDIwLjc2NTYyNX0%3D&sectionManagerState=eyJzZWN0aW9uVHlwZUVuZEluZGV4Ijp7ImFtYWJvdCI6MH19',
    'https://www.amazon.de/primeday/2/ref=gbpp_itr___OURBRAND?gb_f_GB-SUPPLE=MARKETING_ID:amzbPD20&gb_ttl_GB-SUPPLE=Amazon%2520Marken%2520Angebote&ie=UTF8',
    'https://www.amazon.de/primeday/2/ref=gbpp_itr___TVS?gb_f_GB-SUPPLE=enforcedCategories:761254%252C284266&gb_ttl_GB-SUPPLE=TV%2520und%2520Film%2520Angebote&ie=UTF8',
    'https://www.amazon.de/primeday/2/ref=gbpp_itr___SPORTS?gb_f_GB-SUPPLE=enforcedCategories:16435051&gb_ttl_GB-SUPPLE=Sport%2520Angebote&ie=UTF8',
    'https://www.amazon.de/primeday/2/ref=gbpp_itr___TOOLS?gb_f_GB-SUPPLE=enforcedCategories:10925031517801%252C80084031%252C10925031&gb_ttl_GB-SUPPLE=Baumarkt%2520Angebote&ie=UTF8',
    'https://www.amazon.de/primeday/2/ref=gbpp_itr___SMHOME?gb_f_GB-SUPPLE=MARKETING_ID:smartPD20&gb_ttl_GB-SUPPLE=Smart%2520Home%2520Angebote&ie=UTF8',


]

url_input_list_2 = [
    'https://www.amazon.de/blackfriday/2/ref=gbps_ftr___wht_53088303?gb_f_GB-SUPPLE=enforcedCategories:3167641517801%252C530883031,dealTypes:DEAL_OF_THE_DAY%252CBEST_DEAL%252CLIGHTNING_DEAL,sortOrder:BY_SCORE&gb_ttl_GB-SUPPLE=Angebote%2520f%C3%BCr%2520K%C3%BCche%2520und%2520Haushalt&ie=UTF8',
    'https://www.amazon.de/blackfriday/2/ref=gbps_fcr___wht_80084031?gb_f_GB-SUPPLE=enforcedCategories:3167641517801%252C84230031',
    'https://www.amazon.de/blackfriday/2/ref=gbps_fcr___wht_84230031?gb_f_GB-SUPPLE=enforcedCategories:3167641517801%252C80084031',

    'https://www.amazon.de/blackfriday/ref=gbps_ftr___page_1?gb_f_GB-SUPPLE=enforcedCategories:3167641517801%252C84230031,dealTypes:DEAL_OF_THE_DAY%252CBEST_DEAL%252CLIGHTNING_DEAL,sortOrder:BY_SCORE&ie=UTF8',
    'https://www.amazon.de/blackfriday/ref=gbps_ftr___page_2?gb_f_GB-SUPPLE=enforcedCategories:3167641517801%252C84230031,dealTypes:DEAL_OF_THE_DAY%252CBEST_DEAL%252CLIGHTNING_DEAL,page:2,sortOrder:BY_SCORE,dealsPerPage:30&ie=UTF8',
    'https://www.amazon.de/blackfriday/ref=gbps_ftr___page_3?gb_f_GB-SUPPLE=enforcedCategories:3167641517801%252C84230031,dealTypes:DEAL_OF_THE_DAY%252CBEST_DEAL%252CLIGHTNING_DEAL,page:3,sortOrder:BY_SCORE,dealsPerPage:30&ie=UTF8'
]

url_output_list = []

for url in url_input_list_2:
    r = session.get(url)

    r.html.render(sleep=1, keep_page=True, scrolldown=2)

    links = r.html.find('.a-button-text')

    for link in links:
        attributes = link.attrs
        url_path = attributes.get('id')
        if url_path == None:
            continue
        if len(url_path) == 21 and '-announce' in url_path:
            url_id = url_path[-17: -9]
            amz_url = f'https://www.amazon.de/deal/{url_id}/'
            #
            url_output_list.append(amz_url)

print(url_output_list)


