from config import *

def consulta03():
    cursor = conexao.cursor()
    sql = """SELECT uf, COUNT(*)
             FROM cidade
             GROUP BY uf"""

    cursor.execute(sql)

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    for linha in resultados:
        print(linha)
        print('----------------------------------------')