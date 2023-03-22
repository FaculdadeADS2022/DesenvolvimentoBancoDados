from fastapi import FastAPI, HTTPException, status


app = FastAPI(
   title='Barzinho do Irineu, tu não viu, nem eu',
   version='v1.0',
   description='Esta API é usada para comprar pinguinha na esquina.'
   )

@app.get('/msg', 
         description='Mensagem que o Irineu tem pra vuxê bb ;)',
         name='Mensagem do Irineu',response_description='Mensagem recebida com sucesso, seja filiizzz, bjo na bundi! >=D')
async def mensagemIrineu():
   try:
      return {"msg": "Se a vida te der limões, taque num pé de pera, coma uma maçã e se sinta livre!"}
   except Exception:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não vou te falar nada bostão")

@app.get('/somar/{n1}/{n2}', description='Soma quantos reais precisa pra comprar uma pinguinha.')
async def quantosRaeis(n1:int, n2:int):
   return {"soma": f"{n1 + n2}"}

if __name__ == '__main__':
   import uvicorn

   uvicorn.run("main:app", 
               host="0.0.0.0", 
               port=8000, 
               log_level="info", 
               reload=True)