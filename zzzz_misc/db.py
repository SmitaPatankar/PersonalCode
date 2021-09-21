# pip install pyodbc
# download odbc driver for dbms

import pyodbc
for driver in pyodbc.drivers():
    print(driver)
# ODBC 17 driver for sql server

# server
# db

server = "desktop-xxx\SQLEXPRESS"
db = "mydb"

conn_str = "DRIVER={ODBC Driver 17 for SQL Server};" + f"SERVER={server};DATABASE={db};TRUSTED_CONNECTION=yes;"

conn = pyodbc.connect(conn_str)

cursor = conn.cursor()

query = '''insert into table values (?,?);'''
values = ("a", "b")
cursor.execute(query, values)
conn.commit()

# for row in cursor  # tuple
cursor.close()
conn.close()