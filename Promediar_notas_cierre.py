print("---PROMEDIO DE NOTAS HASTA CIERRE---")

# Creo la variable promedio

cantidad = 0
suma = 0

notas = int(input("Ingresa la nota del estudiante (Si colocas -99 se cierra el programa): "))

while notas != -99:
    cantidad = cantidad +1
    suma = suma + notas
    notas = int(input("Ingresa la nota del estudiante (Si colocas -99 se cierra el programa): "))

if notas == -99 and cantidad ==0:
    print("Cantidad:0 , Sin notas")
else:
    promedio = suma / cantidad
    print("Cantidad: ", cantidad, "; Promedio:", promedio)