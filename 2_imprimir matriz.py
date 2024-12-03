def crear_llenar_imprimir_matriz():
    filas = int(input("Introduce el número de filas: "))
    columnas = int(input("Introduce el número de columnas: "))
    matriz = []
    print("Introduce los valores de la matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Introduce el valor para la posición ({i + 1}, {j + 1}): "))
            fila.append(valor)
        matriz.append(fila)
    print("\nLa matriz ingresada es:")
    for fila in matriz:
        print(" ".join(map(str, fila)))
crear_llenar_imprimir_matriz()