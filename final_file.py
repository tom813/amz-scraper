from product_list import product_list


for product_dict in product_list:
    get_perc = product_dict.get("Prozent")
    get_titel = product_dict.get("Titel")
    get_price = product_dict.get("Preis")
    if "-" or "%" in get_perc:
        get_perc = get_perc.replace("-", "").replace("%", "")
    if int(get_perc) < 70 and int(get_perc) > 60:
        print(get_perc, get_titel, get_price)

