# Unidad 1


# Cree una lista de frutas de 7 elementos, y realice un programa que muestre
#  el tercer elemento de la lista en pantalla.

#------------------------------------------------------------------------

# lista = ['string', 'int', 'float', 1, 2, 3, True]

# print('El tercer elemento de la lista es:', lista[2])

#------------------------------------------------------------------------









# Ejercicio 2
 
# Cree una lista de frutas de 2 elementos, y realice un programa que muestre una
#  oración conteniendo los dos elementos de la lista concatenándolos con texto 
# para formar una oración con sentido.

#------------------------------------------------------------------------

# lista_frutas = ['manzana', 'pera']

# print('Caminando por el mercado, pude ver que el precio de la', lista_frutas[0], 'es inferior al de la', lista_frutas[1]+'.')

#------------------------------------------------------------------------









# Ejercicio 3
# Tome un nombre por consola y presente en la pantalla de la consola la
# oración: Hola nombre bienvenido!

#------------------------------------------------------------------------

# name = input('input the name: ')
# print('Hola',name,'bienvenido!')

#------------------------------------------------------------------------











# Ejercicio 4 Tome dos valores por consola, y guarde en una lista:

#------------------------------------------------------------------------

# primer_valor = int(input('Ingrese un valor: '))
# segundo_valor = int(input('Ingrese un segundo valor: '))
# la_suma_de_los_valores = primer_valor + segundo_valor
# lista = [primer_valor, segundo_valor, la_suma_de_los_valores]

#-------------------------------------------------------------------------








# Unidad 2

#Ejercicio 1
# Escriba un programa que consulte al usuario si desea permanecer en
# el sitio web y si la respuesta es afirmativa imprimir en pantalla
# “Bienvenido”, en caso contrario escribir en pantalla “Nos vemos pronto”

#-------------------------------------------------------------------------


# print('Desea permanecer en el sitio web?\n''1 - Si\n''2 - No')
# result = int(input())
# if result==1:
#     print('Bienvenido')
# else:
#     print('Nos vemos pronto')  


# print('Desea permanecer en el sitio web?\n''1 - Si\n''2 - No')
# result = input().lower()
# if result=='si':
#     print('Bienvenido')
# else:
#     print('Nos vemos pronto')   


#-------------------------------------------------------------------------






# Ejercicio 2
# Escriba un programa que solicite el ingreso de un número y muestre en
# pantalla si es par o impar.


#-------------------------------------------------------------------------


# num = int(input('Ingrese un numero: '))
# if num % 2 == 0:
#     print('Es par')
# else:
#     print('No es par')

#-------------------------------------------------------------------------










# Ejercicio 3

# Escriba un programa que consulte por la edad de la persona e informe:
#   Si la persona no está en edad de trabajar.
#   Si la persona está en edad de trabajar, con su edad. 
#   Si la persona está a un año de jubilarse. 

#-------------------------------------------------------------------------

# age = int(input('Ingrese su edad: '))

# if age>100 or age<0:
#     print('Ingrese un numero valido')
# elif age<17 or age>65:
#     print('No esta en edad de trabajar')
# elif age>=18 or age<=64:
#     print('Esta en edad de trabajar')
#     if age==64:
#         print('Y esta a un ano de jubilarse')



#-------------------------------------------------------------------------









# Ejercicio 4
# Escriba un programa que solicite la edad de la persona e imprima todos los
# años que la persona ha cumplido.

#-------------------------------------------------------------------------

# age = int(input('Ingrese su edad: '))

# for i in range(1,age+1):
#     print(i)

#-------------------------------------------------------------------------








# Ejercicio 5

# Escriba un programa que guarde en una variable una contraseña y consulte
# al usuario por la contraseña hasta que esta sea correcta. El programa debe
# informar al usuario si la contraseña fue correcta o no.






#-------------------------------------------------------------------------



# password = '1234asdf'

# while True:
#     user_password = input('Ingrese una contrasena: ')
#     if password == user_password:
#         print('El password es correcto')
#         break
#     else:
#         print('El password es incorrecto, vuelva a intentarlo')
#         continue

#-------------------------------------------------------------------------


# Ejercicio 6

# Escriba un programa que consulte al usuario por una oración y comente al
# usuario cuantas veces aparece la letra “a”. 




#-------------------------------------------------------------------------

word = input('Ingrese una oracion: ')
counter = 0
for i in word:
    if i == 'a':
        counter += 1
print('La vocal "a" se conto', counter, 'veces')


#-------------------------------------------------------------------------

