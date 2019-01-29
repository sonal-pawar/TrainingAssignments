import sqlite3

with sqlite3.connect('BOMBAY_STOCK_EXCHANGE') as db:
    cursor = db.cursor()
    try:
        cursor.execute('''select * from STOCK_MARKET_DATA''')
    except Exception as E:
        print "Error : ", E
    else:
        for row in cursor.fetchall():
            print row
