"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa 
y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también 
funcione cuando el día o el mes se introduzcan con un solo carácter.
"""

fecha = input("Introduce tu fecha de nacimiento dd/mm/aaaa: ")
dia, mes, year = fecha.split("/")

if len(dia) == 1:
    dia = "0" + dia

if len(mes) == 1:
    mes = "0" + mes

print(f"Día: {dia}\nMes: {mes}\nAño: {year}")