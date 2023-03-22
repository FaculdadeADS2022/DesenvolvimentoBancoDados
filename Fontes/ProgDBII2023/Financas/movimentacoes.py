from config import connection
from datetime import date

class movimentacoes:
   idMovimentacao: int
   codTipo: int
   data: date
   observacao: str
   valor: float

   def toTuple(movimentacoes):
      return(movimentacoes.idMovimentacao, 
            movimentacoes.codTipo, 
            movimentacoes.data, 
            movimentacoes.observacao, 
            movimentacoes.valor)

   def insert(movimentacoes):
      cursor = connection.cursor()
      sql = """
               INSERT INTO tipoMovimentacao (idMovimentacao, codTipo, data, observacao, valor)
               values(?, ?, ?, ?, ?)
            """
      data = movimentacoes.toTuple(movimentacoes)
      cursor.execute(sql, data)

      last_id = cursor.lastrowid

      cursor.close()
      connection.close()

      return last_id

   def update(movimentacoes):
      cursor = connection.cursor()
      sql = """
               UPDATE movimentacoes
               SET idMovimentacao = ?,
                  codTipo = ?,
                  data = ?,
                  observacao = ?,
                  valor = ?
            """
      data = movimentacoes.toTuple(movimentacoes)
      cursor.execute(sql, data)

      row_affecteds = cursor.rowcount
      cursor.close()
      connection.close()

      return row_affecteds

   def delete(movimentacoes):
      cursor = connection.cursor()
      sql = """
               DELETE FROM movimentacoes
               WHERE idMovimentacao = ?
            """
      data = movimentacoes.idMovimentacao
      cursor.execute(sql, data)
      cursor.close()
      connection.close()

   def selectAll(movimentacoes):
      cursor = connection.cursor()
      sql = """
               SELECT *
               FROM movimentacoes
            """
      data = movimentacoes.toTuple(movimentacoes)
      cursor.execute(sql, data)

      results = cursor.fetchall
      cursor.close()
      connection.close()

      return results

   def selectById():
      cursor = connection.cursor()
      sql = """
               SELECT idMovimentacao, codTipo, data, observacao, valor
               FROM movimentacoes
               where id = ?
            """
      id = 1
      cursor.execute(sql, id)
      results = cursor.fetchall();

      movimentacoes = movimentacoes()
      for result in results:
         movimentacoes.idMovimentacao = result[0]
         movimentacoes.codTipo = result[1]
         movimentacoes.data = result[2]
         movimentacoes.observacao = result[3]
         movimentacoes.valor = result[4]

      cursor.close()
      connection.close()

      return movimentacoes