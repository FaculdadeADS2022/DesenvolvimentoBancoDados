from config import *

def consulta10():
    cursor = conexao.cursor()
    sql = """SELECT *
             FROM pessoas
             WHERE UPPER(EMAIL) LIKE '%HOTMAIL%'"""

    cursor.execute(sql)

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    for linha in resultados:
        print(linha)
        print('----------------------------------------')