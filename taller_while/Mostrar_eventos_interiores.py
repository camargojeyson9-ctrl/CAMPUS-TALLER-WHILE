
# Pido los dos numeros enteros 
a = int(input("Ingresa el primer numero extremo: "))
b = int(input("Ingresa el segundo numero extremo: "))

# Bucle que mide si el numero a es mayor o igual que b, da error y pide los numeros nuevamente.

while a >= b:
        print("Error, El numero B debe ser mayor que el Numero A")
        input("Presione cualquier tecla para continuar: ")
        a = int(input("Ingresa el primer numero extremo: "))
        b = int(input("Ingresa el segundo numero extremo: "))

# Si sumamos 1 a "a" y es mayor o igual a b, da que no hay numeros enteros para ejecutar los limites, sino realiza la operacion. 

if a+1 >= b:
        print("No hay enteros posteriores")
else:
    for i in range(a+1, b):
        print(i)    

    

