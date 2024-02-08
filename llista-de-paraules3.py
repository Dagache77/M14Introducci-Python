concatenar = ""
while True:
    lletra = input("Introdueix una paraula o final per acabar: ")
    if "final" im lletra:
        break
    else:
        concatenar = concatenar + " "
print(concatenar)
