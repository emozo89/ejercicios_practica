#Desarolle un programa que permita ingresar 20 numeros
#desplegar cuantos son positivos, cuantos negativos y cuantos neutros

ciclos = 20
contador = 1
suma = 0
positivo = 0
negativo = 0
neutro = 0

while contador <= ciclos:
    num = int(input("Ingrese un numero: "))
    contador = contador + 1
    
    if num > 0:
        positivo = positivo + 1
    else:
        if num < 0:
            negativo = negativo + 1
        else:
            neutro = neutro + 1
                
print(f"Los numeros positivos son {positivo} , los numeros negativos son {negativo} , los numeros neutros son {neutro} ")