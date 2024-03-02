print("Calculadora de dos operadores sin comprobacion de errores")
operador1=int(input("Ingrese el operador 1: "))
print(f"El operador 1 es: {operador1}")
operacion=str(input("}Ingrese la operacion a realizar (suma; resta; multiplicacion; division): "))
operador2=int(input("Ingrese el operador 2: "))
print(f"El operador 2 es: {operador2}")
print(f"La operacion seleccionada es {operacion}")
if (operacion == "suma"):
    suma=operador1+operador2
    print(f"La suma es: {operador1} + {operador2} = {suma}")
elif (operacion == "resta"):
    resta=operador1-operador2
    print(f"La resta es: {operador1} - {operador2} = {resta}")
elif (operacion == "multiplicacion"):
    multiplicacion=operador1*operador2
    print(f"La multiplicacion es: {operador1} * {operador2} = {multiplicacion}") 
elif (operacion == "division"):
    division=operador1/operador2
    print(f"La division es: {operador1} / {operador2} = {division}") 
input("Presione ENTER para salir...")