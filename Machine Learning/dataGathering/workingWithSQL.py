import mysql.connector
import pandas as pd

con = mysql.connector.connect(host = "localhost",user = "root", password="",database = "world")

print(pd.read_sql_query("select * from city",con))
