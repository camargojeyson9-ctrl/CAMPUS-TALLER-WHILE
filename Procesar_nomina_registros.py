print("---PROCESAR NOMINA POR REGISTROS---")

while True:
    while True:
        salario = int(input("Ingrese el salario del empleado, (mayor a 0) : "))

        if salario == 0:
            print("Sin trabajadores")
            break

        elif salario > 0:
            break
        else:
            print("El salario debe ser mayor a 0")

    if salario == 0:
        break

    while True:
        dias_trabajados = int(input("Ingrese los dias trabajados por el trabajador, (de 0 a 30 dias):  "))
        if dias_trabajados >= 0:
            break
        else:
            print("Los dias trabajados deben ser igual o mayor a 0")

    while True:
        bonos = int(input("Ingrese los bonos del trabajador en el mes: "))
        if bonos >= 0:
            break
        else:
            print("Los bonos deben ser igual o mayor a 0")

    while True:
        otras_deducciones = int(input("Ingrese las otras deducciones del trabajador en el mes: "))
        if otras_deducciones >= 0:
            break
        else:
            print("Las otras deducciones deben ser igual o mayor a 0")

    while True:
        mensual = int(input("Quieres colocar algun otro valor?, escribe 0 para cerrar el flujo: "))
        if mensual == 0:
            break
        else:
            print("El valor debe ser mayor o igual a 0")
    
    salario_proporcional = salario * dias_trabajados / 30
    devengado = salario_proporcional + bonos
    neto = devengado * 0.83 - otras_deducciones

    print("El salario neto es:",neto)
    break


