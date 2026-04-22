#desarrolle un programa que permita ingresar 10 numeros y al finalizar despliegue el mayor

ciclos = 10
i = 1

num = int(input(f"Ingrese el numero {i}: "))
mayor = num
i = i + 1

while i <= ciclos:
    num = int(input(f"ingrese el número {i}: "))
    i = i + 1
    if num > mayor:
        mayor = num
print(f"El numero mayor es: {mayor}")
