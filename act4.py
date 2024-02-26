llista = [10, 20, 30, 40, 50]

index = (input("Introdueix un número per accedir a la llista:"))
try:
    print(llista[int(index)])
except:
        print("Aquest element no hi és ")
