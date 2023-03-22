from config import *

def consulta02():
    cursor = conexao.cursor()
    sql = """SELECT *
             FROM cidade"""

    cursor.execute(sql)

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    for linha in resultados:
        print(linha)
        print('----------------------------------------')