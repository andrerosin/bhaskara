import math
import os

while True:
    b = float(input("Valor b: "))
    a = float(input("Valor a: "))
    c = float(input("Valor c: "))

    delta = (b**2) -4 * (a * c)

    raiz = math.sqrt(delta)

    print(f"\nResultado delta = {delta}")

    x1 = (-b + raiz) / (2*a)
    print(f"\nResultado x1 = {x1}")

    x2 = (-b - raiz) / (2*a)
    print(f"Resultado x2 = {x2}")

    input("\nPressione ENTER para resetar.")

    os.system("cls")