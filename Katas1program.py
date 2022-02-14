
from turtle import left, right
from numpy import product
from datetime import date

sum = 3 + 4
print(sum)


print('Hola desde la consola')

sum = 1 + 2 # 3
product = sum * 2
print(product)
 
distancia_a_alfa_centauri = 4.367

type(distancia_a_alfa_centauri)

left_side = 10
right_side = 5
left_side / right_side # 2

#Voy entendiendo bien 
date.today()
print(date.today())


print("Today's date is: " + str(date.today()))

print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))