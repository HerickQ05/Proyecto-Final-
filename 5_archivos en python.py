def agregar_contenido_a_archivo(archivo, contenido):
    try:
        with open(archivo, "a") as archivo:
            archivo.write(contenido + "\n")
        print(f"El contenido fue agregado al archivo seleccionado'{archivo}'.")
    except FileNotFoundError:
        print(f"El archivo no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
archivo = input("Introduce el nombre del archivo con extension: ")
contenido = input("Introduce el contenido que deseas agregar: ")
agregar_contenido_a_archivo(archivo, contenido)