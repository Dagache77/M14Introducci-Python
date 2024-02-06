num = int(input("Introdueix un número per veure la seva taula de multiplicar: "))

contador = 1

while contador <= 10:
    resultat = num * contador
    print(f"{num} x {contador} = {resultat}")
    contador += 1
