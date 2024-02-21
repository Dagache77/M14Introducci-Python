import random

def tirada_dau():
    return random.randint(1, 6)

def daus_6():
    n_tirades = int(input("Quant daus vols llençar: "))

    for _ in range(n_tirades):
        resultat = tirada_dau()
        print(f"Resultat de la tirada: {resultat}")

# Executar el programa
daus_6()
