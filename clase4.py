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