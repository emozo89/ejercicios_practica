i = 1
resultado = int(input("ingrese un numero: "))
while i <=9:
    numero = int(input("ingrese un numero: "))
    if resultado < numero:
        resultado = numero
    i = i + 1
print("el numero mayor es: ", resultado)

