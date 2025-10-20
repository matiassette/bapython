# clase 2:
# en esta parte se aprende a generar saltos de codigo segun los espacios de la variable
# print("nombre1:\tMatias\nEdad:\t34")
# lo que estoy haciendo es un salto de linea con \t esto hace que las plabras sean
# saltos de linea mientras mas largo sea el nombre o digito mas espacios se generan
# entre salto por eso la salida de matias 34 es mucho ya que el nombre matias
# ocupa 6 espacios en codigo
# salida:
# nombre: matias
# edad: 34

# print("Producto\tPrecio")
# print("Manzanas\t$ 1.00")
# print("Peras\t\t$ 1.50")

# en este apartado se usa el end
# print("hola,", end=' ')
# print("mundo")
# salida: hola, mundo
# lo que hace el end es imroimir el finla de la cadena lo que significa que cada llamada a print
# termina con un salto de linea

# comando para ingresar datos de la persona de forma escrita no por defecto ya ingresada
# por el programador
# nombre = input("ingrese su nombre: ")
# print("hola ", nombre)

# conversion de enteros a flotantes
# ejemplo de int a float en este ejemplo se transforma un numero entero a flotante
# entero = 10
# decimal = float (entero)
# print (decimal)
# la salida por pantalla es 10.0

# conversion de numeros flotantes a enteros
# decimal = 3.14
# entero = int (decimal)
# print (entero)
# la salida por pantalla es 3

# conversion de numeros acadenas de caracteres y viceversa
# ejemplo de int a str

# edad = 25
# mensaje = "tengo " + str(edad) + " años."
# print (mensaje)

# con esto lo que hago es concatenar osea asociar letras y numeros en una sola linea
# la salida por pantalla es tengo 25 años

# ejemplo de str a int
# cadena_numerica = "123"
# numero = int (cadena_numerica)
# print (numero + 7)

# en este caso int cadena_numerica convierte la cadena de caracteres "123" a un numero entero 123
# esto permite realizar operaciones de suma resta multi ext

# valor_verdadero = True
# valor_falso = False
# print(int(valor_verdadero))
# print(int(valor_falso))

# aqui true se convierte en 1 y el fasle se convierte en 0 esto es muy util en los calculos q dependen
# de condiciones logicas

# ejemplo de int a boleano

# numero = 0
# print (bool(numero))
# numero = 5
# print (bool(numero))

# cualquier numero distinto a 0 se convierte a true  en una conversion booleano mientras que 0 se
# convierte a false

# funcion type

# numero = 42
# print (type(numero))

# precio = 19.99
# print (type(precio))

# mensaje = "hola, mundo"
# print (type(mensaje))

# esMayorDeEdad = True
# print (type(esMayorDeEdad))

# cada llamado de type() te devuelve el tipo del valor asignado a la variable: int para enteros
# float para flotantes, str para cadenas de texto  y bool para booleanos.

# edad = input ("introduce tu edad: ")
# edad = int(edad)
# print ("el proximo año tendras ", edad + 1, "años. ")

# esto hace que al ingresar un numero q esta en la variable edad como str lo cambie a int
# haciendo que el numero que ya viene por teclado se le sume un numero

# operadores aritmeticos
# suma
# resultado = 5 + 3
# print (resultado)
# resta
# resultado = 5 - 3
# print (resultado)
# multiplicacion
# resultado = 5 * 3
# print (resultado)
# division
# resultado = 5 / 3
# print (resultado)

# en la division el resultado retorna un numero flotante incluso si el resultado es entero

#division entera (//): divide el 1 valor entre el 2 y redondea el resultado hacia abajo para
# obtener un numero entero (int)

# resultado = 7 // 3
# print (resultado)

#modulo (%): retorna o devuelve el sobrante de la division entre el primer y segundo valor

# resultado = 7 % 3
# print (resultado)

#exponenciacion (**): eleva el 1 valor a la potencia del 2

# resultado = 2 ** 3
# print (resultado)

"""
ejercicio practico de la clase 2

Hola

En nuestro dia a dia, interactuamos con muchos clientes, y uno de los pasos iniciales es recopilar y organizar su informacion basica. Para eso, necesito que desarrolles un pequeño programa en python que haga lo siguiente:

1) Solicite al cliente su nombre, apellido, edad y correo electronico.
2) Almacene estos datos en variables.
3) Los muestre organizados en forma de una tarjeta de presentacion en la pantalla.

Espero ver el resultado de tu trabajo pronto.

saludos 
mariana.
"""

# print ("Hola mi nombre es matias tu asistente personal,") 
# print ("bienvenido al programa donde se le solicitaran un par de datos personales.")
# nombre = input ("Ingrese su nombre:\t ")
# nombre = str(nombre)
# apellido = input("Ingrese su apellido:\t ")
# apellido = str (apellido)
# edad = input("Ingrese su edad:\t ")
# edad = int (edad)
# correo_electronico = input("Ingrese su correo electronico:\t ")
# correo_electronico = str(correo_electronico)

# print ("Hola ")
# print ("Nombre: ", nombre)
# print ("Apellido: ", apellido)
# print ("Edad: ", edad)
# print ("Correo electronico: ", correo_electronico)
# print ("Gracias por usar este programa.")
# print ("Te esperamos la proxima")


# x,y,z = 1,2,3
# print (x+y+z)