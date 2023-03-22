from config import *

def consulta06():
    cursor = conexao.cursor()
    sql = """SELECT pessoas.NOME, 
                    pessoas.ENDERECO, 
                    pessoas.TELEFONE,
                    pessoas.CELULAR,
                    cidade.NOME,
                    pessoas.NASCIMENTO
             FROM pessoas
                 JOIN cidade ON(cidade.id = pessoas.cidade)
             WHERE cidade.uf = 'PR'"""

    cursor.execute(sql)

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    for linha in resultados:
        print(linha)
        print('----------------------------------------')