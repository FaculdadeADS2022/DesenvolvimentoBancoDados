from config import *

def consulta05():
    cursor = conexao.cursor()
    sql = """SELECT *
             FROM pessoas
             ORDER BY nascimento DESC
             LIMIT 1"""

    cursor.execute(sql)

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    for linha in resultados:
        print(linha)
        print('----------------------------------------')