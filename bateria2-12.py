num = int(input("Introdueix un número: "))

suma = 0

for i in range(1, num + 1):
    suma += i

print(f"La suma dels números fins a {num} és: {suma}")
