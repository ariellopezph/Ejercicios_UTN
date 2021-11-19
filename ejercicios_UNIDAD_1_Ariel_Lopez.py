# Cree una lista de frutas de 7 elementos, y realice un programa que muestre el tercer elemento de la lista en pantalla.

lista = ['string', 'int', 'float', 1, 2, 3, True]

print('El tercer elemento de la lista es:', lista[2])

# Ejercicio 2
 
# Cree una lista de frutas de 2 elementos, y realice un programa que muestre una oración conteniendo los dos elementos de la lista concatenándolos con texto para formar una oración con sentido.

lista_frutas = ['manzana', 'pera']

print('Caminando por el mercado, pude ver que el precio de la', lista_frutas[0], 'es inferior al de la', lista_frutas[1]+'.')
name = input('input the name: ')

# Ejercicio 3
# Tome un nombre por consola y presente en la pantalla de la consola la oración:
# Hola nombre bienvenido!

print('Hola',name,'bienvenido!')

# Ejercicio 4 Tome dos valores por consola, y guarde en una lista:

primer_valor = int(input('Ingrese un valor: '))
segundo_valor = int(input('Ingrese un segundo valor: '))
la_suma_de_los_valores = primer_valor + segundo_valor
lista = [primer_valor, segundo_valor, la_suma_de_los_valores]
