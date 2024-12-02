def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
num = int(input("Ingresa un número entero positivo: "))
if num < 0:
    print("El número debe ser positivo.")
else:
    print(f"El factorial de {num} es: {factorial(num)}")