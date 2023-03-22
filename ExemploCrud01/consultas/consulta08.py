from config import *

def consulta08():
    cursor = conexao.cursor()
    sql = """SELECT * 
             FROM pessoas
             WHERE ATIVO = 1
             ORDER BY TELEFONE"""

    cursor.execute(sql)

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    for linha in resultados:
        print(linha)
        print('----------------------------------------')