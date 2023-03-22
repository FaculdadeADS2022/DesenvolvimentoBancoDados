from config import *

def consulta07():
    cursor = conexao.cursor()
    sql = """SELECT cidade.nome, COUNT(*)
             FROM cidade
                 INNER JOIN pessoas ON(pessoas.cidade = cidade.id)
             GROUP BY cidade"""

    cursor.execute(sql)

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    for linha in resultados:
        print(linha)
        print('----------------------------------------')