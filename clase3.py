# clase 3 condicionales
# operadores relacionados
# tambien se conocen como operadores de compracion, sirven para algo clave:
# comparar valores. el resultado de esta comparacion siempre es booleano, es decir true (verdadero) y false (falso)

# operador    significado         descripcion
#     ==      igual que           verifica el valor o los valores de 2 expresiones son iguales
#     !=      no igual que        comprueba si 2 valores son diferentes
#     >       mayor que           evalua si el valor de la izq es mayor que el valor de la derecha
#     <       menor que           determina si el valro de la izq es mayor o menor que el valor de la derecha
#     >=      mayor o igual que   verifica si el valor de la izq es mayor o igual al valor de la derecha
#     <=      menor o igual que   comprueba si el valor de la izq es menor o igual al valor de la derecha

# ejemplos

# print (3 > 4)
# print (2 <= 4)
# print (2 != 22)
# print ("Hola" == "hola")
# print ("Carlos" < "Ada")

# == (igual que): verifica si 2 cadenas son exactamente iguales
# != (no igual que):comprueba si 2 cadenas son diferentes
# > (mayor que), <(menor que):compara las cadenas segun el valor de cada caracter.

# este tipo de comparacion se llama orden lexicografico. python va caracter por caracter sdesde el principio de 
# las 2 cadenas comparando. si encuentra alguna diferencia, ahi se detiene y decide cual es "mayor" o "menor"
# si las cadenas son identicas hasta cierto punto pero una es mas corta. entonces la mas corta se considera "menor"

# print ("apple" < "banana")
# print ("apple" > "Apple")
# print ("apple" < "apples")

# print ("python" == "python")
# print ("Python" != "python")

# print ("A" < "a")
# print ("z" > "Z")

# operador "and"
# solo devuelve true si todas las condiciones que esta evaluando son verdaderas. basta con que una sola sea falsa
# para que el resultado total sea false. es como decir "quiero que todo lo que estoy evaluando cumpla con la condicion"

# resultado = (5 > 3) and (8 > 6)
# print (resultado)

# resultado = (5 > 3) and (8 < 6)
# print (resultado)

# operador "or"
# operador or por otro lado es un poco mas relajado. con el, alcanza con que una sola de las condiciones sea verdaderas
# para que el resultado total sea True. sola va a devolver False si todas las condiciones on falsas. es como decir 
# "si al menos una cosa cumple, esta bien"

# resultado = (5 > 3) or (8 < 6)
# print (resultado)

# resultado = (5 < 3) or (8 < 6)
# print (resultado)

# operador "not"
# finalmente tenemos el operador not. este es el que invierte el valor de verdad de una expresion. si algo es True
# not lo convierte en false y viceversa. es como un interruptor de luz: lo que esta prendido lo apaga, y lo que esta
# apagado lo prende.

# resultado = not (5 > 3)
# print (resultado)

# resultado = not (5 < 3)
# print (resultado)

# control de flujo: estructuras condicionales

# imagina que estas caminando por la calle y de repente comienza a llover en ese momento tenes que tomar una decision
# rapida: si tenes paraguas lo abris si no salis corriendo para no mojarte. bueno en programacion las estructuras
# condicionales son algo muy parecido. le dicen al programa que hacer dependiendo de lo que este ocurriendo en el 
# instante. en python usamos estas estructuras para que el codigo pueda tomar decisiones segun lo que este pasando
# o segun los datos que reciba.

# numero = 5

# if numero > 0:
#     print ("El numero es positivo: ")

# edad = 18

# if edad >= 18:
#     print ("Sos mayor de edad.")

# en este ejemplo estamos verificando si alguien tiene 18 años o mas. si la condicion es true, python va a imprimir
#  "sos mayor de edad. " si no, simplemente va a seguir con el resto del programa, sin hacer nada especial con esa linea.

# estructura condicional con if y else

# hasta ahora vimos como if le da la capacidad a tu programa de tomar decisiones cuando una condicion es verdadera. pero
#  ¿que pasa cuando esa condicion no se cumple ? ahi es donde entra en juego else. mientras que el if se encarga de ejecutar
# un bloque de codigo solo si algo es true. else viene al rescate cuando una condicion resulta ser falsa.
# es como decir si pasa esto hace tal cosa y si no hace tal otra.

# numero = -5

# if numero > 0:
#     print ("El numero es positivo.")
# else:
#    print ("El numero no es positivo.")

# edad = 16
# if edad >= 18:
#     print ("Sos mayor de edad.")
# else:
#     print ("Sos menor de edad.")

# como usar el else

# en lugar de tener que escribir mas if o manejar los casos por separado, else te permite cubrir todos los escenarios
# posibles es los que la condicion no se cumple, lo que hace que tu codigo sea mas eficiente y facil de leer . ademas
# le da al programa la capacidad de reaccionar de manera distinta segun los datos que reciba o el estado en el
# que este

# precio = 450
# if precio < 500:
#     print ("El producto es economico.")
# else:
#     print ("El producto es costoso.")

# edad = 20
# es_ciudadano = True

# if edad >= 18 and es_ciudadano:
#     print ("Podes votar. ")
# else:
#     print ("No podes votar. ")

# en esta parte del programa lo que se intenta hablar es sobre el ("#") que sirve para documentar o comentar el programa
# base = 5
# altura = 10
# area = base * altura
# print ("El area es: ", area)

# comentarios multilinea
# se identifican con 3 comillas simple aunque estas cadenas estan diseñadas para definir textos largos dentro 
# del codigo , se utilizan comunmente como comentarios para explicar procesos mas complejos.

# """
# Este programa calcula el area de un rectangulo.
# Primero define la base y la altura.
# Luego multiplica ambos valores para obtener el area.
# Finalmente, muestra el resultado en pantalla
# """

# base = 5
# altura = 10
# area = base * altura
# print ("El area es: ", area)

"""
Ejercicio practico.
Luego de un dia intenso en Talentolab. y gracias a la ayuda inestimable de luis, ya podes intentar resolver
la tarea que te encargo mariana. Como siempre, te escribo un correo explicando detalladamente que necesita que hagas.

!Hola!

Necesito que desarrolles un pequeño programa en python que haga exactamente lo siguiente:

Solicite al cliente su nombre, apellido, edad y correo electronico.
Compruebe que el nombre, el apellido y el correo no esten en blanco, y que la edad sea mayor de 18 años.
Muestra los datos por la terminal , en el orden que se ingresaron. Si alguno de los datos ingresados no 
cumplen los requisitos, solo mostrar el texto "ERROR:".

¡Espero ver el resultado de tu trabajo pronto!

Saludos,
Mariana
"""

# nombre = input("Ingrese su nombre : ")
# apellido = input ("Ingrese su apellido: ")
# correo_electronico = input ("Ingrese su correo electronico: ")
# edad = int (input("Ingrese su edad: "))
# if nombre != "" and apellido != "" and correo_electronico != "" and edad >= 18:
#     print ("El nombre es: ", nombre)
#     print ("El apellido es: ", apellido)
#     print ("El correo electronico es: ", correo_electronico)
#     print ("Su edad es: ", edad, "años")
# else:
#     print("ERROR")
    # print("falta poner:",nombre,"nombre")
    # print("falta poner:", apellido,"apellido")
    # print("falta poner:", correo_electronico,"correo electronico")
    # print("La edad es menor a la necesaria: ",edad, "ingrese de nuevo la edad")

