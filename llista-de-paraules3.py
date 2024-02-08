concatenar = ""
while True:
    lletra = input("Introdueix una paraula o final per acabar: ")
    if "final" in lletra:
        break
    else:
        concatenar = (concatenar+ lletra + " ")
print(concatenar)
