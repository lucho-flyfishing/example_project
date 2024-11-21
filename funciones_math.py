import math  # importat libreria para operaciones matematicas

x = 1.054 
print(round(x)) #redondear el valor de la funcion x
print(round(x,2)) #redondear indicando cifras decimales
print(math.ceil(x)) #redondear para arriba
print(math.floor(x)) #redondear para abajo
print(math.trunc(x)) #la parte entera de un decimal

numeros = [1,2,3,4,5]
print(math.fsum(numeros)) #sumar los numeros de una lista
print(int(math.fsum(numeros))) #entrega el valor entero del parametro de la funcion
print(math.fabs(-4)) #valor absoluto del parametro de la funcion
print(math.exp(2)) #eleva el valor de epsilon al valor del parametro
print(math.pow(5,6)) #eleva el primer parametro al valor del segundo parametro (5^6)
print(math.sqrt(16)) #raiz cuadrada de el valor del parametro

h = math.hypot(1.5, 1.5) #calcula la hipotenusa de un triangulo con catetos del valor de los parametros
print(h) 

r = math.radians(45)
print('Valor en radianes: {0}'.format(r))

print(math.sqrt(25))