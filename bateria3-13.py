num = int(input("Introdueix un número: "))

suma = 0

for i in range(2, num + 1, 2):
    suma += i

print(f"La suma dels números parells fins a {num} és: {suma}")

