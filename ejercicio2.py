#datos
ipc_febrero = 0.3
ipc_marzo = 0.6

#entrada
precio_base = int(input("Ingrese el valor del producto: "))

#proceso
precio_febrero = precio_base + ipc_febrero
precio_marzo = precio_base + ipc_marzo
diferencia = precio_marzo - precio_febrero

#salida
print(f"La diferencia entre febrero y marzo fue de {diferencia}, el precio de febrero fue de {precio_febrero}, y en marzo el precio fue de {precio_marzo}")
