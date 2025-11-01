import pytest
from calculator import Calculator

calc = Calculator()

def test_sumar():
    assert calc.sumar(3, 2) == 5

def test_restar():
    assert calc.restar(10, 4) == 6

def test_multiplicar():
    assert calc.multiplicar(3, 5) == 15

def test_dividir():
    assert calc.dividir(8, 2) == 4

def test_dividir_por_cero():
    try:
        calc.dividir(5, 0)
        assert False  # si no lanza error, falla el test
    except ZeroDivisionError:
        assert True

