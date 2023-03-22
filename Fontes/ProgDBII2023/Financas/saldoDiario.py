from config import connection
from datetime import date

class saldodiario:
   data: date
   valor: float

   def toTuple(saldodiario):
      return(saldodiario.data, saldodiario.valor)

   def insert(saldodiario):
      cursor = connection.cursor()
      sql = """
               INSERT INTO saldodiario (data, valor)
               values(?, ?)
            """
      data = saldodiario.toTuple(saldodiario)
      cursor.execute(sql, data)

      last_id = cursor.lastrowid

      cursor.close()
      connection.close()

      return last_id

   def update(saldodiario):
      cursor = connection.cursor()
      sql = """
               UPDATE saldodiario
               SET data = ?,
                  valor = ?
            """
      data = saldodiario.toTuple(saldodiario)
      cursor.execute(sql, data)

      row_affecteds = cursor.rowcount
      cursor.close()
      connection.close()

      return row_affecteds

   def delete(saldodiario):
      cursor = connection.cursor()
      sql = """
               DELETE FROM saldodiario
               WHERE data = ?
            """
      data = saldodiario.data
      cursor.execute(sql, data)
      cursor.close()
      connection.close()

   def selectAll(saldodiario):
      cursor = connection.cursor()
      sql = """
               SELECT *
               FROM saldodiario
            """
      data = saldodiario.toTuple(saldodiario)
      cursor.execute(sql, data)

      results = cursor.fetchall
      cursor.close()
      connection.close()

      return results

   def selectById():
      cursor = connection.cursor()
      sql = """
               SELECT data, valor
               FROM saldodiario
               where data = ?
            """
      data = saldodiario.toTuple(saldodiario)
      cursor.execute(sql, data)
      results = cursor.fetchall();

      saldodiario = saldodiario()
      for result in results:
         saldodiario.data = result[0]
         saldodiario.valor = result[1]

      cursor.close()
      connection.close()

      return saldodiario