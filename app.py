from fastapi import FastAPI, HTTPException
from calculator import Calculator
import os

app = FastAPI(title="Calculadora")
calc = Calculator()

@app.get("/")
def root():
    return {"ok": True, "servicio": "calculadora", "endpoints": ["/sumar","/restar","/multiplicar","/dividir"]}

@app.get("/sumar")
def sumar(a: float, b: float):
    return {"resultado": calc.sumar(a, b)}

@app.get("/restar")
def restar(a: float, b: float):
    return {"resultado": calc.restar(a, b)}

@app.get("/multiplicar")
def multiplicar(a: float, b: float):
    return {"resultado": calc.multiplicar(a, b)}

@app.get("/dividir")
def dividir(a: float, b: float):
    try:
        return {"resultado": calc.dividir(a, b)}
    except ZeroDivisionError as e:
        raise HTTPException(status_code=400, detail=str(e))
