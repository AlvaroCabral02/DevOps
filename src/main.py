from fastapi import FastAPI
app = FastAPI()

@app.get("/calcular")
def calcular(operacao: str, a: float, b: float):

    if operacao == "soma":
        return {"resultado": a + b}

    if operacao == "subtracao":
        return {"resultado": a - b}

    if operacao == "multiplicacao":
        return {"resultado": a * b}

    if operacao == "divisao":
        if b == 0:
            return {"erro": "divisão por zero"}
        return {"resultado": a / b}

    return {"erro": "operação inválida"}