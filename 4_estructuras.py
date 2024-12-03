def estudiante(nombre, edad, promedio):
    return {
        "nombre": nombre,
        "edad": edad,
        "promedio": promedio
    }
def imprimir_datos(estudiante):
    print("Detalles del estudiante:")
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Edad: {estudiante['edad']}")
    print(f"Promedio: {estudiante['promedio']:.2f}")
if __name__ == "__main__":
    nombre = input("Introduce el nombre del estudiante: ")
    edad = int(input("Introduce la edad del estudiante: "))
    promedio = float(input("Introduce el promedio del estudiante: "))
    estudiante = estudiante(nombre, edad, promedio)
    imprimir_datos(estudiante)