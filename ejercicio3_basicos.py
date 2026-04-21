#Solicitud de datos

print("\nBienvenido al sistema de calculo de IVA")
precio_neto = int(input("Ingrese el monto de su factura: "))

#Calculo/proceso

iva = precio_neto * 0.19
precio_bruto = precio_neto * 1.19

#salida

print(f"\n El iva de su factura es {iva} y el total bruto de su compra es de {precio_bruto}")
print("---Gracias por su compra---")