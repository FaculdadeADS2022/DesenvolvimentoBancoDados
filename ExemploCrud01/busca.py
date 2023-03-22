from config import *

sql = "select * from pessoas"
cursor = conexao.cursor()

cursor.execute(sql)

resultados = cursor.fetchall()

cursor.close()
conexao.close()

for linha in resultados:
    print(str(linha[0]) + '\b' + linha[1] + '\t' + (str(linha[2])))
    print('----------------------------------------')