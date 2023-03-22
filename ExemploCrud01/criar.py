from datetime import datetime
from config import *

cursor = conexao.cursor()

sql = """insert into pessoas (nome, endereco, telefone, celular, 
                              email, cpf, cidade, nascimento)
                       values(%s, %s, %s, %s, 
                              %s, %s, %s, %s)"""

dados = (
    "Tomzinho",
    "Rua Beatriz",
    "4635362525",
    "46991264072",
    "tomzinho@cometudo.com.br",
    "10808229923",
    1100015,
    datetime(1997, 3, 11)
)

cursor.execute(sql, dados)
conexao.commit()

cursor.close()
conexao.close()

print('Novo registro incluído com sucesso!')