#print("---Bienvenido al programa de registro curricular---")
#num1 = float(input("Ingrese su nota:"))
#num2 = float(input("Ingrese su nota:"))
#num3 = float(input("Ingrese su nota:"))
#num4 = float(input("Ingrese su nota:"))
#num5 = float(input("Ingrese su nota:"))
#num6 = float(input("Ingrese su nota:"))
#num7 = float(input("Ingrese su nota:"))

#prom = (num1+num2+num3+num4+num5+num6+num7) / 7

#if prom >=4:
#    print(f"Su promedio {prom:.1f} es aceptable")
#else:
#    print(f"Su promedio {prom:.1f} no es suficiente para aprobar")
#print("fin")    

print("---Bienvenido al programa de registro curricular---")

suma = 0
i = 1

while i <= 7:
    nota = float(input(f"Ingrese la nota {i}: "))
    suma = suma + nota
    i += 1

prom = suma / 7

if prom >= 4:
    print(f"Su promedio {prom:.1f} es aprobado")
else:
    print(f"Su promedio {prom:.1f} es reprobado")

print("fin")