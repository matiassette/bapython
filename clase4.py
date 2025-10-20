# estructuras condicionales avanzadas: elif

# el bloque elif(abreviatura de "else if")nos permite manejar multiples casos dentro de una misma estructura condicional
# , evitando redundancias y haciendo que nuestro codigo sea mas eficiente y legible.

# sintaxis basica de elif

# edad = 25

# if edad < 13:
#     print ("Son menores a trece años: ")
# elif edad < 18:
#     print ("Sos un o una adolescente. ")
# elif edad < 60:
#     print ("Sos una persona adulta. ")
# else:
#     print ("Sos una persona adulta mayor")

# usamos elif cuando 
# 1) hay multiples condiciones mutuamente excluyente (es decir solo una puede ser verdadera)
# 2) queremos evitar escribir varios bloques if independientes que podrian complicar el seguimiento del codigo

# nota = int (input("Ingrese la nota del o de la estudiante: "))
# if nota >= 90:
#     print ("Excelente.")
# elif nota >= 75:
#     print ("Muy bien.")
# elif nota >= 60:
#     print ("Bien.")
# elif nota >=40:
#     print ("Suficiente.")
# else:
#     print ("Insuficiente.")

# este ejemplo muestra como elif permite manejar facilmente varias categorias sin repetir codigo innecesariamente

# combinando elif con operadores logicos

# edad = int(input("Ingresa tu edad: "))
# ingreso = int(input("Escribi tu ingreso mensual: "))
# if edad < 18:
#     print ("Sos menor de edad. ")
# elif edad >= 18 and ingreso < 50000:
#     print ("Sos mayor de edad, pero tenes ingresos bajos")
# elif edad >= 18 and ingreso >= 50000:
#     print ("Sos mayor de edad y tenes ingresos altos")
# else:
#     print ("Datos no validos.")

# este programa clasifica a las personas segun su edad y nivel de ingresos, mostrando como elif se combina 
# con operadores para resolver problemas mas realistas.

# estructura condicional avanzada: match 
# la estructura match fue introducida como una alternativa mas clara y poderosa al uso de multiples bloques if
# elif,else especialmente cuando queremos comparar un valor especifico con varias opciones posbiles. es similar a la 
# estructura switch de otros lenguajes de programacion y se utiliza para simplificar el manejo de los casos multiples

# la sintaxis general de match es:

# match variable:
#     case valor1:
#         #codigo si variable coincide con valor1
#     case valor2:
#         #codigo si variable conincide con valor2
#     case _:
#         #codigo si no coincide ningun caso (opcional)

# variable: es el valor que queremos comparar. puede ser de cualquier tipo, como numeros, cadenas, tuplas,etc
# case valor1: define un caso especifico. si variable coincide con este valor, se ejecuta el bloque de codigo asociado
# _(guion bajo):representa el caso por defecto, que se ejecuta si no hay coincidencia con ninguno de los casos anteriores
# es equivalente al else en un bloque condicional.

# fruta = input ("ingresa una fruta: ")
# match fruta:
#     case "manzana":
#         print ("Es una fruta roja o verde")
#     case "banana":
#         print ("Es una fruta amarilla ")
#     case "naranja":
#         print ("Es una fruta anarajanda")
#     case _:
#         print ("No tengo informacion sobre esta fruta")

# un ejemplo entre match y if

# con if elif

# dia = 3
# if dia == 1:
#     print ("Lunes")
# elif dia == 2:
#     print ("Martes")
# elif dia == 3:
#     print ("Miercoles")
# else:
#     print ("Dia no valido")

# con match

# dia = 3
# match dia:
#     case 1:
#         print ("Lunes")
#     case 2:
#         print ("Martes")
#     case 3:
#         print ("Miercoles")
#     case _:
#         print ("Dia no valido")

""" !hola!
a partir de lo que has aprendido, intenta escribir un programa que clasifique paquetes segun su peso. el programa
debe solicitar que se ingrese el peso del paquete (en kilogramos) y, en base al valor ingresado. clasificar 
el paquete en una de las siguientes categorias:
1 paquete pequeño:para paquetes que pesan hasta 5 kg inlusive
2 paquete mediano: para paquetes cuyo peso sea mayor a 5 kg y hasta  20 kg inclusive 
3 paquete grande: para paquetes que pesan mas de 20 kg
4 paquete no valido: en caso de que el peso ingresado sea negativo o no corresponda a un valor numerico valido"""

# peso = float(input("ingrese el peso del paquete(en kg)"))
# match peso:
#     case p if p <= 5:
#         print ("paquete pequeño")
#     case p if 5 < p <= 20:
#         print ("paquete mediano") 
#     case p if p > 20:
#         print ("paquete grande")
#     case _:
#         print ("paquete no valido")

# concatenacion de cadenas

# es el proceso de unir dos o mas cadenas de texto para formar una nueva. en python, podes usar el operador + para 
# lograrlo de manera mas sencilla.
# cuando trabajas con datos textuales, la concatenacion es una herramienta clave. por ej, podes combinar el nombre
#  y el apellido de una persona para mostrar su nombre completo en pantalla.

# nombre = "maria"
# apellido = "gonzalez"

# nombre_completo = nombre + " " + apellido
# print (nombre_completo)

# en este ejemplo se guarda la concatenacion de nombre + apellido y se lo visualiza con la variable nueva nombre completo

# saludo = "hola"
# nombre = "lucia"
# mensaje = saludo + ", " + nombre + ", ¿como estas?"
# print (mensaje)

# en este caso combinamos 3 cadenas: saludo, nombre y una cadena literal (el texto desntro de comillas). usamos comas,
# espacios y signos de puntuacion para hacer que el mensaje tenga sentido y sea amigable

# si necesitas unir una cadena con otro tipo de dato, como un numero o un valor booleano, primero tenes que convertir 
# ese dato en texto usando la funcion str(). esto es necesario porque , como sabes, python no permite combinar distintos
# tipos de datos directamente.

# edad = 30
# mensaje = "tenes " + str(edad) + " años."
# print (mensaje)

# en este caso la variable edad es un numero entero( tipo int) por lo que usamos str (edad) para convertirlo en texto.
# luego, concatenamos la cadena resultante con otras cadenas para formar el mensaje final.

# longitud de una cadena de caracteres y la funcion len()
# la longitud de una cadena de caracteres es la cantidad total de caracteres que contiene.
# esto incluye letras, numero, espacios, simbolos y cualquier otro caracter que forme parte del texto. en python, podes 
# determinar la longitud de una cadena utilizando la funcion incorporada len()

# la funcion len() toma como argumento una cadena y devuelve un numero entero que representa la cantidad de cracteres de esa cadena

# mensaje = "hola, mundo"
# print (len(mensaje))

# la cadena "hola mundo" tiene 11 caracteres en total, contadno el espacio y la coma. python incluye todos los caracteres 
# visibles y no visibles (como los espacios) en la longitud.
# podes usar len() para asegurarte que se ingrese un dato valido. por ejemplo, evitar un campo como "nombre" quede vacio.

# nombre = input("ingrese su nombre: ")
# if len(nombre) == 0:
#     print ("el nombre no puede ser vacio")
# else:
#     print("hola, " + nombre + "!")

# al no ingresar datos sale por el else.
# algunas aplicaciones requieren que un dato, como una contraseña, tenga cierta cantidad de caracteres. podes valida esto con len()
# contraseña = input ("ingrese su contraseña: ")
# if len(contraseña) < 8:
#     print("la contraseña debe tener al menos 8 caracteres")
# else:
#     print("contraseña valida.")

# rompiedo cadenas
# las cadenas en python no son mas que una secuencia ordenada de caractere. esta caracteristica es muy util cuando
# necesitas trabajar con partes especificas de un texto, como extraer una letra, analizar un segmento o incluso 
# modificar el formato de ciertas secciones.

# esto sifgnifica que el primer caracter de la cadena tiene posicion 0 el segundo tiene la poscion 1 y asi sucesivamente
# podes utilizar la notacion con corchetes [] para acceder a un caracter especifico.
# mensaje = "hola", podes acceder al primer caracter escribiendo mensaje[0]

# mensaje = "hola"
# print (mensaje[0])

# print (mensaje[3])

# una de las grandes ventajas de esta funcionalidad es que tambien podes usar indice negativo, python empieza a contar 
# desde el final de la cadena.

# mensaje = "hola"
# print (mensaje[-1])

# print(mensaje[-2])

# lo que sucede es que esta contando de atras para adelante es como un espejo.

# podes extraer una porcion de la cadena utilizando slicing(rebanado). esto se hace indicando un rango en los corchetes
# [inicio:fin]. el rango incluye el caracter en la posicion de inicio, pero no del fin. si escribis el mensaje[0:2] 
# vas a obtener "ho", que incluye los caracteres de la posion 0 y 1, pero no de la posicion 2. si omitis el inicio o el fin
# del rango, python asume que queres ir desde el principi hasta el final de la cadena, respectivamente. por ejemplo, mensaje
# [:2] te devuelvo "ho" y mensaje[1:] te da "ola"

# print (mensaje[0:2])
# print( mensaje[1:])
# print(mensaje[:2])

# esta herramienta podes utilizarla para validar texto, formatearlo o analizarlo con mucha precision. ej si quisiera verificar
# si una cadena empieza con cierta letra, podrias hacer algo como mensaje[0] == "h" y eso te devolveria true si el 1
# er caracter es "h"

# metodos de cadenas en python

# lo interesante de este metodo es que no modifica la cadena original si no que genera una nueva con los cambios aplicados
# ej
# .lower()
# texto = "hola mundo"
# print(texto.lower())
# convierte todos los caracteres de la cadena a minusculas. ideal para hacer comparaciones insensibles a mayusc o minus
# .upper()
# texto = " hola mundo"
# print(texto.upper())
# convierte todo el texto a mayusculas.util para normalizar texto antes de guardarlo o precesarlo
# .title()
# texto = " hola mundo"
# print(texto.title())
# .strip()
# texto = " hola mundo"
# print(texto.strip())
# elimina los espacios en blanco al principio y al final de la cadena
# .replace()
# texto = " hola mundo"
# print(texto.replace())
# reemplaza una sub cadena por otra adentro de la cadena
# .startswitch()
# texto = " hola mundo"
# print(texto.startswitch())
# devuelve true si la cadena comienza con la subcadena especifica, de lo contrario devuelve false
# .endswitch()
# texto = " hola mundo"
# print(texto.endswitch())
# devuelve true si la cadena termina con la subcadena especifica, de lo contrario devuelve False
# .find()
# texto = " hola mundo"
# print(texto.find())
# devuelve la posicion de la primera aparicion de una subcadena dentro de la cadena, o -1 si no la encuntra
# .isdigit()
# texto = " hola mundo"
# print(texto.title())
# devuelve un valor booleano true si todos los valores de la cadena de entrada son digitos, de lo contratio false
# solicitamos al usuario que confirme si esta seguro
