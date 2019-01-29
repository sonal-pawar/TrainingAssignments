import sqlite3
from web_api import web_interface


def get_result():
    stock_dict = web_interface.web_api()
    for key, value in stock_dict.iteritems():
        stock_code = str(key)
        company_name = str(value.get('company_name'))
        previous_day = str(value.get('top_1').get('date'))
        closing_price_previous_day = str(value.get('top_1').get('value'))
        two_days_back = str(value.get('top_2').get('date'))
        closing_price_two_days_back = str(value.get('top_2').get('value'))
        profit_or_loss = str(value.get('profit'))
        stock_list1 = [(stock_code, company_name, previous_day, closing_price_previous_day, two_days_back,
                        closing_price_two_days_back, profit_or_loss)]
        with sqlite3.connect('BOMBAY_STOCK_EXCHANGE') as db:
            cursor = db.cursor()
            try:
                pass
                cursor.execute('''CREATE TABLE STOCK_MARKET_DATA 
                (STOCK_CODE TEXT, COMPANY_NAME TEXT, PREVIOUS_DAY TEXT, CLOSING_PRICE_PREVIOUS_DAY TEXT, 
                TWO_DAYS_BACK TEXT, CLOSING_PRICE_TWO_DAYS_BACK TEXT, PROFIT_OR_LOSS TEXT)''')
                print "Table created"
                sql = ''' INSERT INTO STOCK_MARKET VALUES (?,?,?,?,?,?,?)'''
                cursor.executemany(sql, stock_list1)
                print "record inserted"

            except Exception as E:
                print "Error : ", E
            else:
                db.commit()


get_result()








