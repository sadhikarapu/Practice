import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=learnazurecontent.database.windows.net;'
                      'Database=Stock_Analysis;'
                      'UID=sqladmin;'
                      'PWD=LiveStrong@2021'
                      )

cursor = conn.cursor()

query_top_100 = cursor.execute("Select top 100 * from stock_prices where stock_ticker_name='HDFC'")

for i in query_top_100:
    print(i)
