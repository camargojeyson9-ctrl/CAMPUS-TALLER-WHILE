print("---SUMAR LECTURAS CENTINELA---")

suma = 0

# Input que pide el numero.
num = int(input("Ingresa un numero para realizar las operaciones, hasta que coloques - 50: "))

# Si el usuario escribe -50 se cierra el bucle y se suma los numeros ingresados.
while num != -50:
    suma = suma + num
    num = int(input("Ingresa un numero para realizar las operaciones, hasta que coloques - 50: "))

print("suma:", suma)

    


