from fastapi import FastAPI
import random
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
  
#testes de Ps
 @app.get("/teste")
async def funcaoteste():
    return {"teste": true, "num_aleatorio": random.randint(1, 1000)}