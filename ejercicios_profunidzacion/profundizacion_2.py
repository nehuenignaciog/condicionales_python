# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA:
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio


# Ingrese tres números cualesquiera

numero_1 = int(input("Ingrese el primer número:\n"))

numero_2 = int(input("Ingrese el Segundo número:\n"))

numero_3 = int(input("Ingrese el Tercer número:\n"))

# Creo funcion que dedvuelve si es par o impar


def par_impar(numero):
    if (numero % 2):
        return "Impar"
    else:
        return "Par"


# Imprimo en pantalla el resultado para cada caso

print ("El primer numero ({}) es {}".format(numero_1, par_impar(numero_1)))
print ("El Segundo numero ({}) es {}".format(numero_2, par_impar(numero_2)))
print ("El Tercer numero ({}) es {}".format(numero_3, par_impar(numero_3)))
 