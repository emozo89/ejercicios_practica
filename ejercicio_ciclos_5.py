#Desarrolle un programa que permita ingresar 15 numeros negativos, los convierta a positivos
#e imprima dichos numeros

ciclos = 15
contador = 1 
negativo = []

while contador <= 15:
    num = int(input(f"Ingrese el numero {contador}: "))
    contador = contador + 1
    negativo.append(num)
    
    if num > 0:
        num = num * -1
        
print(f"Los numeros: {negativo} son negativos")
        