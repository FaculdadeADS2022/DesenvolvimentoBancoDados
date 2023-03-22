from config import *

def consulta01():
    cursor = conexao.cursor()
    sql = """SELECT *
             FROM pessoas
             WHERE nascimento <= DATE_SUB(CURRENT_DATE, INTERVAL 18 YEAR)"""

    cursor.execute(sql)

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    for linha in resultados:
        print(linha)
        print('----------------------------------------')