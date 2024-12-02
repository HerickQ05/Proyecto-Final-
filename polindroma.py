import string

def palindroma(cadena):
    cadena_filtrada = ''.join(char.lower() for char in cadena if char.isalnum())
    return cadena_filtrada == cadena_filtrada[::-1]
cadena = input("Introduce una frase: ")
if palindroma(cadena):
    print("Es palíndroma")
else:
    print("No es palíndroma")