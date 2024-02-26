# Demana a l'usuari que introdueixi un número, i intenta convertir aquesta entrada en un enter. Utilitza try i except per capturar qualsevol error de conversió.

entrada = input("Introdueix un nombre: ")
try:
    sortida = int(entrada)
except:
    print("Has introduit un nombre no valid")
