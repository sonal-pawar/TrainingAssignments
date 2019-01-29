import requests
import logging
import sys
import json


def web_api():
    # "BOM539597", "BOM500397"
    stocks = ["BOM539597", "BOM539397", "SPICBLOT", "SPBSB2IP", "SPBSN5IP", "SPBSS5IP", "BOM539658", "BOM539874", "BOM539678", "BOM539450"]

    auth_key = "uQssnxWZyynoy2jWLyXV"

    stocks_dict = {}

    for row in stocks:
        print row
        url = "https://www.quandl.com/api/v3/datasets/BSE/{}.json?api_key={}".format(row, auth_key)
        print url
        logging.basicConfig(format="%(levelname)-10s: %(message)s",
                            filename="webApi.log", filemode='w',
                            level=logging.DEBUG)

        logging.debug('complete url is: {}'.format(url))

        response = requests.get(url)

        if response.status_code != 200:
            logging.error("Error: response is {}".format(response))
            sys.exit(1)

        content = json.loads(response.content)

        logging.info('Company info: {}'.format(content.get('dataset').get('name')))
        stocks_dict[row] = {"company_name": content.get('dataset').get('name')}
        stocks_dict[row]["stock_values"] = []

        for data in content.get('dataset').get('data'):
            data_dict = dict()
            data_dict['date'] = data[0]
            data_dict['value'] = data[4]
            stocks_dict[row]['stock_values'].append(data_dict)

        stocks_dict[row]['top_1'] = stocks_dict[row]['stock_values'][0]
        stocks_dict[row]['top_2'] = stocks_dict[row]['stock_values'][1]
        profit_or_loss = True if stocks_dict[row]['top_1']['value'] >= stocks_dict[row]['top_2']['value'] else False
        stocks_dict[row]['profit'] = profit_or_loss
        del stocks_dict[row]['stock_values']

    return stocks_dict


web_api()
