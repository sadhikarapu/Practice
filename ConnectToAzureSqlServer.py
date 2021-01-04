import pyodbc
import pandas as pd

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=learnazurecontent.database.windows.net;'
                      'Database=Stock_Analysis;'
                      'UID=sqladmin;'
                      'PWD=LiveStrong@2021'
                      )

query_top_100 = "Select top 100 * from stock_prices where stock_ticker_name='HDFC'"

pd_query = pd.read_sql_query(query_top_100,conn)

column_df = list(pd_query.columns)

df = pd.DataFrame(pd_query)

pd.set_option('display.max_columns',7)

