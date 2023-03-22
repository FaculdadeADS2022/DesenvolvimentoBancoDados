from datetime import datetime
from config import *

cursor = conexao.cursor()

sql = """
    update pessoas set nome = %s, 
                        endereco = %s,
                        telefone = %s, 
                        celular = %s, 
                        email = %s, 
                        cpf = %s, 
                        cidade = %s,
                        nascimento = %s
    where pessoas.id = %s"""

dados = (
    "TomzinhoLiroPiro",
    "Rua Beatriz Love",
    "4635362530",
    "46991264072",
    "tomzinho@hotmail.com",
    "10808229923",
    1100015,
    datetime(1997, 3, 11),
    6
)

cursor.execute(sql, dados)
conexao.commit()

linhasAfetadas = cursor.rowcount

cursor.close()
conexao.close()

print(str(linhasAfetadas) + ' registros alterados com sucesso!')