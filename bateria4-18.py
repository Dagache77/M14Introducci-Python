numero = int(input("Introdueix un número: "))
suma_impares = 0

for i in range(1, numero + 1, 2):
    suma_impares += i

print(f"\nLa suma dels números imparells fins a {numero} és: {suma_impares}")
