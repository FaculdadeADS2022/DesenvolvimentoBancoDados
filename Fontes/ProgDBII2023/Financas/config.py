import mysql.connector as mysql
from datetime import date

connection = mysql.connect(
   host="localhost",
   user="root",
   password="tomateseco",
   database="bar_do_neu",
   port=3306
)