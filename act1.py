# Pregunta a l'usuari dos nombres i divideix-los. Utilitza un bloc try i except per evitar l'error de divisió per zero.
num1 = int(input("Introdueix un número: "))
num2 = int(input("Introdueix un altre número: "))
try:
    a = num1 / num2
    print(a)

except:
    print("Error")
