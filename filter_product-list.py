
bsp_list = [{'Prozent': '-48%', 'Titel': 'Versandoption', 'Preis': '11,99'}, {'Prozent': '-54%', 'Titel': 'Kategorie', 'Preis': '12,59'}, {'Prozent': '-39%', 'Titel': 'BeliebigeKategorie', 'Preis': '36,49'}, {'Prozent': '-29%', 'Titel': 'Spielzeug', 'Preis': '10,99'}, {'Prozent': '-46%', 'Titel': 'Baby', 'Preis': '10,99'}, {'Prozent': '-52%', 'Titel': 'Sport&Freizeit', 'Preis': '5,99'}]

for product_dict in bsp_list:
    x = product_dict.get("Prozent")
    y = product_dict.get("Titel")
    if "-" or "%" in x:
        x = x.replace("-", "").replace("%", "")
    if int(x) > 50:
        print(x, y)