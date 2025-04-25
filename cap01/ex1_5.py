"""
Programa que verifica a paridade de um número que o utilizador insere
"""

n = int(input("Vamos verificar a paridade do número: "))

msg = "ímpar"

if n % 2 == 0:
    msg = "par"

print(f"{n} é {msg}")
