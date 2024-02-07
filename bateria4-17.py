suma = 0
contador = 0

while True:
    num = float(input("Introdueix un número (0 per acabar): "))
    
    if num == 0:
        break  
    else:
        suma += num
        contador += 1

if contador == 0:
    print("No s'ha introduït cap número.")
else:
    mitjana = suma / contador
    print(f"\nMitjana dels números introduïts: {mitjana}")
