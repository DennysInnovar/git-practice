"""Pequeña calculadora usada para el Reto 5 (git bisect).

Ejecuta este archivo directamente para correr las auto-pruebas:
    python ejercicios/03-historial/app.py

Si todo está bien, imprime "OK" y termina con código 0.
Si algo está roto, lanza un AssertionError y termina con código != 0.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    # BUG: se cambió el operador por error durante una "optimización"
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


if __name__ == "__main__":
    assert add(2, 3) == 5
    assert subtract(5, 3) == 2
    assert multiply(4, 3) == 12
    assert divide(10, 2) == 5
    print("OK")
