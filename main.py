from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
#testes de Ps
 @app.get("/teste")
async def root():
    return {"teste": "deu certo"}