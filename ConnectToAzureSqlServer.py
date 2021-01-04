import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=learnazurecontent.database.windows.net;'
                      'Database=Stock_Analysis;'
                      'UID=sqladmin;'
                      'PWD=LiveStrong@2021'
                      )

cursor = conn.cursor()

print(type(cursor))