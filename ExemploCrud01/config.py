import mysql.connector as mysql

conexao = mysql.connect(
    host="localhost",
    user="root",
    password="tomateseco",
    database="pgi_teste01",
    port=3306
)

print('Banco de dados conectado com sucesso!')