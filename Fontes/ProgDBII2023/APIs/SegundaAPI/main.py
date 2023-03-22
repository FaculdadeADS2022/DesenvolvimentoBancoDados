from typing import (
   Dict,
   List,
   Optional,
   Any
)

from fastapi import (
   FastAPI, 
   HTTPException, 
   status,
   Response,
   Path,
   Query,
   Header,
   Depends
)

from fastapi.responses import JSONResponse

from models import Curso, cursos

app = FastAPI(
   title="Api de cursos",
   version="1.0.1",
   description="Uma API especial para pessoas especiais."
)

@app.get('/cursos', 
         description = "Retorna todos os cursos",
         summary = "Todos os cursos",
         response_model = List[Curso],
         response_description = "Funfou!")
async def get_cursos():
   return cursos;

@app.get('/curso/{curso_id}',
         response_model=Curso)
async def get_curso(curso_id: int = Path(default = None, 
                                       title = "Id do curso", 
                                       description = "Deve ser entre 1 e 2", 
                                       gt=0, 
                                       lt=10)):
   try:
      curso = cursos[curso_id]
      return curso
   except KeyError:
      raise HTTPException(
         status_code = status.HTTP_404_NOT_FOUND,
         detail="Curso não encontrado"
      )

@app.get('/curso', status_code = status.HTTP_201_CREATED, response_model = Curso)
async def post_curso(curso: Curso):
   next_id: int = len(cursos) + 1
   curso.id = next_id
   cursos.append(curso)
   return curso

if __name__ == '__main__':
   import uvicorn

   uvicorn.run("main:app", 
               host="0.0.0.0", 
               port=8000, 
               log_level="info", 
               reload=True)