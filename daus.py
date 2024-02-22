import random

def tirada_dau(cara_max):
    return random.randint(1, cara_max)

def daus_x(cara_max, num_tirades):
    for _ in range(num_tirades):
        resultat = tirada_dau(cara_max)
        print(f"Resultat de la tirada: {resultat}")


cara_max = int(input("Quantes cares té el dau: "))
num_tirades = int(input("Quant daus vols llençar: "))
daus_x(cara_max, num_tirades)
