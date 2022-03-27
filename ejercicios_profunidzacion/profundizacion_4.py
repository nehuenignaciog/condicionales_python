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

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

# Declaro funciones de ordenamiento

def ordenar_alfabetico(valor_1,valor_2,valor_3):
   
    if (valor_2 < valor_1 and valor_3 < valor_1):
        orden_1 = valor_1
        if (valor_2 < valor_3):
            orden_3 = valor_2
            orden_2 = valor_3
        else:
            orden_3 = valor_3
            orden_2 = valor_2
    elif (valor_1 < valor_2 and valor_3 < valor_2):
        orden_1 = valor_2
        if (valor_1 < valor_3):
            orden_3 = valor_1
            orden_2 = valor_3
        else:
            orden_3 = valor_3
            orden_2 = valor_1
    else:
        orden_1 = valor_3
        if (valor_1 < valor_2):
            orden_3 = valor_1
            orden_2 = valor_2
        else:
            orden_3 = valor_2
            orden_2 = valor_1
 
    print("\nOrden Alfabetico\n")
    print ("1 - {}\n".format(orden_3))
    print ("2 - {}\n".format(orden_2))
    print ("3 - {}\n".format(orden_1))
   
def ordernar_cantidad_letras(valor_1, valor_2, valor_3):
   len_valor_1= len(valor_1)
   len_valor_2= len(valor_2)
   len_valor_3= len(valor_3)
   if (len_valor_2 < len_valor_1 and len_valor_3 < len_valor_1):
        orden_1 = valor_1
        if (len_valor_2 < len_valor_3):
            orden_3 = valor_2
            orden_2 = valor_3
        else:
            orden_3 = valor_3
            orden_2 = valor_2
   elif (len_valor_1 < len_valor_2 and len_valor_3 < len_valor_2):
        orden_1 = valor_2
        if (len_valor_1 < len_valor_3):
            orden_3 = valor_1
            orden_2 = valor_3
        else:
            orden_3 = valor_3
            orden_2 = valor_1
   else:
        orden_1 = valor_3
        if (len_valor_1 < len_valor_2):
            orden_3 = valor_1
            orden_2 = valor_2
        else:
            orden_3 = valor_2
            orden_2 = valor_1
 
   print("\nOrden por cantidad de letras (mayor a menor) \n")
   print ("1 - {}\n".format(orden_1))
   print ("2 - {}\n".format(orden_2))
   print ("3 - {}\n".format(orden_3))

# Solicito Ingreso de palabras

print ("Por favor ingrese tres palabras cualesquiera.")

texto_1 = str(input('Ingrese la primera:\n')).lower()

texto_2 = str(input('Ingrese la segunda:\n')).lower()

texto_3 = str(input('Ingrese la tercera:\n')).lower()

# Imprimo menú de opciones

print ("\nPor favor seleccione el ordenamiento.\n")
print ("1 - Ordenar por orden alfabético\n" )
print ("2 - Ordenar por cantidad de letras\n")
opcion = str(input())



# Imprimo resultado

if (opcion == '1'):
    ordenar_alfabetico (texto_1,texto_2,texto_3)

elif (opcion == '2'):
    
     ordernar_cantidad_letras(texto_1,texto_2,texto_3)
    
else:
    print ("Seleccion incorrecta. Por favor vuelva a ejecutar el programa.")

