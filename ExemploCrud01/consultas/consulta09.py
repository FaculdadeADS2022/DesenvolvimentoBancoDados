from config import *

def consulta09():
    cursor = conexao.cursor()
    sql = """SELECT cidade.nome, cidade.uf
             FROM cidade
                 LEFT OUTER JOIN pessoas ON(pessoas.cidade = cidade.id)
             WHERE pessoas.id IS NULL"""

    cursor.execute(sql)

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    for linha in resultados:
        print(linha)
        print('----------------------------------------')