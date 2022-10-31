# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import datetime


def main(quant=1, currency='Евро'):
    url = 'https://www.raiffeisen.ru/currency_rates/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    text = soup.get_text()
    splitted_text = text.split()
    counter = 0
    for key in splitted_text:
        counter += 1
        if key == currency:
            selling_price = splitted_text[counter]
            selling_price = float(selling_price)
            selling_price = round(selling_price, 2)
            print("Цена покупки на", datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y"), "=", selling_price)
            break

    total_zp = quant * selling_price
    return [round(total_zp, 3), datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y")]


if __name__ == "__main__":
    main()
