# Pregunta a l'usuari dos valors i intenta sumar-los. Utilitza try i except per capturar errors quan els valors no són números.
num1 = (input("Introdueix un número: "))
num2 = (input("Introdueix un altre número: "))

try:
    resultat = float(num1) + float(num2)
    print(resultat)

except:
    print("Error")
