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

texto_1 = texto_1.lower()
texto_2 = texto_2.lower()


# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

if (texto_1 > texto_2):
    print ("Primer palabra mayor ({} > {}).".format(texto_1, texto_2))
elif (texto_2 > texto_1):
    print ("Segunda palabra mayor ({} > {}).".format(texto_2, texto_1))
else:
    print ("Palabras son iguales ({} = {}).".format(texto_1, texto_2))


# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

len_tex_1 = len(texto_1)
len_tex_2 = len(texto_2)

if (len_tex_1 > len_tex_2):
    print ("Primer palabra con mas letras ({} > {}).".format(len_tex_1, len_tex_2))
elif (len_tex_2 > len_tex_1):
    print ("Segunda palabra con mas letras  ({} > {}).".format(len_tex_2, len_tex_1))
else:
    print ("Palabras con igual cantidad de letras ({} = {}).".format(len_tex_1, len_tex_2))

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

inicial_texto_1 = str(texto_1)[0]

inicial_texto_2 = str(texto_2)[0]


if (inicial_texto_1 == inicial_texto_2):
    print ("Iniciales iguales ({} = {}).".format(inicial_texto_1, inicial_texto_2))
else:
    print ("Iniciales distintas ({} != {}).".format(inicial_texto_1, inicial_texto_2))

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

if (copia_texto_1 == texto_1):
    print("copia_texto_1 es igual a texto_1".format(copia_texto_1, texto_1))
else:
    print("copia_texto_1 es distinto a texto_1".format(copia_texto_1, texto_1))

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if (copia_texto_1 == texto_2):
    print("copia_texto_1 es igual a texto_2".format(copia_texto_1, texto_2))
else:
    print("copia_texto_1 es distinto a texto_2".format(copia_texto_1, texto_2))
