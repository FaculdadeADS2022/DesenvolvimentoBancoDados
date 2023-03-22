from typing import Optional

from pydantic import BaseModel, validator

class Curso(BaseModel):
   id: Optional[int] = None
   nome: str
   aulas: int #mais de 15
   horas: int #mais de 30

   @validator('nome')
   def validar_titulo(cls, value: str):
      palavras = value.split(" ")
      if len(palavras) < 2:
         raise ValueError('Informe pelo menos duas palavras.')
      
      if value.islower():
         raise ValueError('Informe pelo menos as iniciais em maiúsculo.')

      return value

   @validator('aulas')
   def validar_aulas(cls, value: int):
      if(value < 15):
         raise ValueError('É necessário possuir 15 aulas ou mais.')

      return value

   @validator('horas')
   def validar_horas(cls, value: int):
      if(value < 30):
         raise ValueError('É necessário possuir mais de 30 horas aula.')
      return value


cursos = [
   Curso(id = 1, nome="Programação 1 basica", aulas = 40, horas = 80),
   Curso(id = 2, nome="Programação 2 media", aulas = 20, horas = 40),
   Curso(id = 3, nome="Programação 3 avançada", aulas = 15, horas = 80),
   Curso(id = 4, nome="Programação 4 monster", aulas = 25, horas = 30),
   Curso(id = 5, nome="Programação 5 ultra", aulas = 30, horas = 333),
   Curso(id = 6, nome="Manutenção de ar condicionado", aulas = 100, horas = 250),
]