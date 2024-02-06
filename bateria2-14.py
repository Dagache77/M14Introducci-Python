num = int(input("Introdueix un número: "))

opcio = input("Vols sumar els números parells o senars? (p/s): ")

suma = 0

if opcio.lower() == 'p':
    for i in range(2, num + 1, 2):
        suma += i
    tipus_numeros = 'parells'
elif opcio.lower() == 's':
    for i in range(1, num + 1, 2):
        suma += i
    tipus_numeros = 'senars'
else:
    print("Opció no vàlida. Si us plau, introdueix 'p' per parells o 's' per senars.")
    exit()

print(f"La suma dels números {tipus_numeros} fins a {num} és: {suma}")
