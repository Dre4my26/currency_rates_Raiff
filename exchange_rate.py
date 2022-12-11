# -*- coding: windows-1251 -*-

import datetime
import requests as req
import json


def main(quant=1, currency=['EUR']) -> list:
    currencies = currency
    rate_list = []
    curr_rate = []  # list of [<currencyName>, <rateToRUB>]
    string_curr = ','.join(map(str, currency))
    a = req.get(f"https://www.raiffeisen.ru/oapi/currency_rate/get/?source=RCONNECT&currencies={string_curr}")
    result = json.loads(a.text)
    for i in range(len(currencies)):
        price = result['data']['rates'][0]['exchange'][i]['rates']['buy']['value']
        rate_list.append(price)
    curr_rate.append(currencies)
    curr_rate.append(rate_list)
    final_list = [curr_rate[1][0], datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y")]
    return final_list


data_row = str(main()[0]) + ',' + str(main()[1])


def data_to_csv():
    f = open('time_rate.csv', mode='a', newline='')
    f.write(data_row + '\n')
    f.close()

    return 0


if __name__ == "__main__":
    print("Цена покупки на", datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y"), "=", main()[0])
    main()
    data_to_csv()
