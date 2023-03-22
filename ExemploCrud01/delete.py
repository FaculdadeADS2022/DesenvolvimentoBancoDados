from config import *

cursor = conexao.cursor()

sql = "delete from pessoas where pessoas.id = 6"

cursor.execute(sql)

linhasDeletadas = cursor.rowcount

cursor.close()
conexao.close()

print(str(linhasDeletadas) + ' registro(s) apagado(s) com sucesso!')