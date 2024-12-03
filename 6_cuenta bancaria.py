class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso\nNuevo saldo: {self.saldo:.2f}")
        else:
            print("El monto a depositar debe ser mayor que cero.")
    def retirar(self, monto):
        if monto > 0:
            if monto <= self.saldo:
                self.saldo -= monto
                print(f"Retiro exitoso\nNuevo saldo: {self.saldo:.2f}")
            else:
                print("Saldo insuficiente.")
        else:
            print("El monto a retirar debe ser mayor que cero.")
    def mostrar_saldo(self):
        print(f"El saldo actual de la cuenta de {self.titular} es: {self.saldo:.2f}")
if __name__ == "__main__":
    nombre = input("Introduce el nombre del titular de la cuenta: ")
    saldo_inicial = float(input("Introduce el saldo inicial: "))
    cuenta = CuentaBancaria(nombre, saldo_inicial)
    while True:
        print("\nOpciones:")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Mostrar saldo")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            monto = float(input("Introduce el monto a depositar: "))
            cuenta.depositar(monto)
        elif opcion == "2":
            monto = float(input("Introduce el monto a retirar: "))
            cuenta.retirar(monto)
        elif opcion == "3":
            cuenta.mostrar_saldo()
        elif opcion == "4":
            print("Gracias por usar el sistema bancario")
            break
        else:
            print("Opción no válida")