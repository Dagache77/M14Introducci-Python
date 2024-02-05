factorial = int(input("Digues un número per calcular el seu valor factorial: "))
resultat = 1
for i in range(1,factorial+1):
    resultat = resultat * i
print("El resultat és", resultat)
