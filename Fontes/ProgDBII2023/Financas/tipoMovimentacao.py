from config import connection

class tipoMovimentacao:
   id: int
   descricao: str
   tipo: str

   def toTuple(tipoMovimentacao):
      return(tipoMovimentacao.id, tipoMovimentacao.descricao, tipoMovimentacao.tipo)

   def inserir(tipoMovimentacao):
      cursor = connection.cursor()
      sql = f"""
               INSERT INTO tipoMovimentacao (descricao, tipo)
               values('{tipoMovimentacao.descricao}', '{tipoMovimentacao.tipo}')
            """
      cursor.execute(sql)

      last_id = cursor.lastrowid

      connection.commit()
      cursor.close()
      connection.close()

      return last_id

   def update(tipoMovimentacao):
      cursor = connection.cursor()
      sql = f"""
               UPDATE tipoMovimentacao
               SET descricao = '{tipoMovimentacao.descricao}',
                  tipo = '{tipoMovimentacao.tipo}'
               WHERE id = {tipoMovimentacao.id}
            """
      cursor.execute(sql)

      row_affecteds = cursor.rowcount
      connection.commit()
      cursor.close()
      connection.close()

      return row_affecteds

   def delete(tipoMovimentacao):
      cursor = connection.cursor()
      sql = """
               DELETE FROM tipoMovimentacao
               WHERE id = ?
            """
      data = tipoMovimentacao.id
      cursor.execute(sql, data)
      cursor.close()
      connection.close()

   def selectAll(tipoMovimentacao):
      cursor = connection.cursor()
      sql = """
               SELECT *
               FROM tipoMovimentacao
            """
      data = tipoMovimentacao.toTuple(tipoMovimentacao)
      cursor.execute(sql, data)

      results = cursor.fetchall
      cursor.close()
      connection.close()

      return results

   def selectById():
      cursor = connection.cursor()
      sql = """
               SELECT id, descricao, tipoMovimentacao
               FROM tipoMovimentacao
               where id = ?
            """
      id = 1
      cursor.execute(sql, id)
      results = cursor.fetchall();

      tipo = tipoMovimentacao()
      for result in results:
         tipo.id = result[0]
         tipo.descricao = result[1]
         tipo.tipoMovimentacao = result[2]

      cursor.close()
      connection.close()

      return tipo