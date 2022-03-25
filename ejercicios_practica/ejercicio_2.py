# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

texto_1=texto_1.lower()
texto_2=texto_2.lower()


# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

if (texto_1 > texto_2):
    print ("La primer palabra es mayor ({} > {}).".format(texto_1, texto_2))
elif (texto_2 > texto_1):
    print ("La segunda palabra es mayor ({} > {}).".format(texto_2, texto_1))
else:
    print ("Las palabras son iguales ({} = {}).".format(texto_1, texto_2))


# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

cantidad_letras_1= len(texto_1)
cantidad_letras_2=len(texto_2)

if ( cantidad_letras_1> cantidad_letras_2):
    print ("La primer palabra tiene mas letras ({} > {}).".format(cantidad_letras_1, cantidad_letras_2))
elif (cantidad_letras_2 > cantidad_letras_1):
    print ("La segunda palabra tiene mas letras  ({} > {}).".format(cantidad_letras_2, cantidad_letras_1))
else:
    print ("Las palabras tienen la misma cantidad de letras ({} = {}).".format(texto_1, texto_2))



# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

inicial_texto_1=texto_1[0]

inicial_texto_2=texto_2[0]



if (inicial_texto_1 > inicial_texto_2):
    print ("La inicial de la primer palabra es mayor ({} > {}).".format(inicial_texto_1, inicial_texto_2))
elif (inicial_texto_2 > inicial_texto_2):
    print ("La inicial de la segunda palabra es mayor ({} > {}).".format(inicial_texto_2, inicial_texto_1))
else:
    print ("Las iniciales son iguales ({} = {}).".format(inicial_texto_1, inicial_texto_2))



copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

if (copia_texto_1 == texto_1):
    print("copia_texto_1 es igual a texto_1".format(copia_texto_1,texto_1))
else:
    print("copia_texto_1 es distinto a texto_1".format(copia_texto_1,texto_1))

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if (copia_texto_1 == texto_2):
    print("copia_texto_1 es igual a texto_2".format(copia_texto_1,texto_2))
else:
    print("copia_texto_1 es distinto a texto_2".format(copia_texto_1,texto_2))
