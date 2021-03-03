from config.conf import PAIDAN_DB_QA
import mysql.connector

mydb = mysql.connector.connect(PAIDAN_DB_QA)

print(mydb)