print("---Bienvenido al programa de registro curricular---")
num1 = float(input("Ingrese su nota:"))
num2 = float(input("Ingrese su nota:"))
num3 = float(input("Ingrese su nota:"))
num4 = float(input("Ingrese su nota:"))
num5 = float(input("Ingrese su nota:"))
num6 = float(input("Ingrese su nota:"))
num7 = float(input("Ingrese su nota:"))

prom = (num1+num2+num3+num4+num5+num6+num7) / 7

if prom >=4:
    print(f"Su promedio {prom} es aceptable")
else:
    print(f"Su promedio {prom} no es suficiente para aprobar")
print("fin")    