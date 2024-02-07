numero = int(input("Introdueix un número: "))

print(f"\nDivisors de {numero}:\n")
for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        print(divisor)
