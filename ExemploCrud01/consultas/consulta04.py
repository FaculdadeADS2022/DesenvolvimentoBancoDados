from config import *

def consulta04():
    cursor = conexao.cursor()
    sql = """SELECT *
             FROM pessoas
             ORDER BY nascimento
             LIMIT 1"""

    cursor.execute(sql)

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    for linha in resultados:
        print(str(linha[0]) + '\b' + linha[1] + '\t' + (str(linha[2])))
        print('----------------------------------------')