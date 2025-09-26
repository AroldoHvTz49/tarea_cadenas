"""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
 y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""

precio = input("Ingrese el precio del producto: ")

if "." in precio:
    euros, centimos = precio.split(".")
else:
    euros = precio
    centimos = "00"

print(f"El precio es de {euros} Euros y {centimos} Céntimos")
