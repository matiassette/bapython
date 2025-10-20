# nombre = (input("ingree su nombre: ")).strip()

# while (nombre == ""):
#     print("ERROR")
#     nombre = input("por favor re ingrese su nomre: ")
#     nombre = nombre.strip()
    
# print(f"nombre: {nombre}")

# numero = 1

# while (numero <= 20):
#     print (f"(numero)")
#     if (numero % 3 == 0 and numero % 5 == 0):
#         break
#     numero +=1
    
# print (f"{numero} es divisible por 3 y 5 ")

# numero = 0
# suma = 0

# while True:
#     numero = int(input("ingrese un numero positivo: (o para terminar): "))
    
#     if (numero < 0):
#         print(f"numero negativo")
#         continue
#     elif(numero == 0):
#         break
#     else:
#         suma = suma + numero
#         print(f"{suma}")
        
# print(f"total : {suma}")

# numero = [2,5,6,8]

# datos_alumno = ["juan","gonzalez",23,1.70,True]

# frutas = ["frutilla", "cereza", "naranja" , "pera"]

# cont = 0

# while(cont < len(frutas)):
#     print(frutas[cont])
#     cont +=1
# print(f"terminado / contador: {cont}")

# print(frutas[1])
# print(frutas[1:3])
# print(f"cantidad de elementos: {len(frutas)}")

"""opcion 1 de resolucion del problema"""

"""Para este ejercicio necesitamos un software que ayude a registrar y calcular información financiera básica para nuestros y nuestras clientes.

Tu tarea para esta semana es la siguiente:

Registrar los ingresos mensuales de un cliente durante 6 meses. Usá un bucle while para solicitar el ingreso de cada mes.Validar que los ingresos sean números positivos. Si se ingresa un valor negativo, mostrá un mensaje indicando que el valor no es válido y volvé a pedir el dato.

Calcular el total acumulado durante los 6 meses. Mostrá este resultado al final del programa.

El programa debe mostrar el apellido, nombre y dirección de correo con el formato pedido, y el texto correspondiente a su rango etario.

¡Estoy segura de que harás un excelente trabajo!

Saludos, Mariana

"""

# while (contador < 6):
#     pago_mes = int(input("ingrese su saldo (de 6 meses)"))
#     contador += 1

#     if (numero_veces < 6):
#         continue
#     elif(numero_veces == 0):
#         break
#     else:
#         suma_total = pago_mes + suma_total

# print(f"total : {suma_total}")

# contador = 1
# ingreso = 0
# suma = 0

# while (contador <= 6):
#     ingreso = float(input(f"ingrese su ingreso {contador}:" ))
#     while (ingreso < 0):
#         print ("ERROR valor negativo de ingreso invalido")
#         ingreso = float(input(f"ingrese su ingreso {contador}:"))
        
#     suma = suma + ingreso
#     contador +=1
    
# print("a continuacion se pide ingresar datos")
# print(f"total: {suma}")

# nombre = ""
# apellido = ""
# mail = ""
# edad = 0

# print("a continuacion se le pedira unos datos: ")
# nombre = input("ingrese su nombre: ")
# apellido = input("ingrese su apellido: ")
# mail = input("ingrese su mail: ")
# edad = int(input("ingrese su edad :"))

# if edad <= 18:
#     print ("sos menor de edad,", edad)
#     print("su nombre es: ", nombre)
#     print("su apellido es:", apellido)
#     print("su mail: ", mail)
#     print("sos menor de edad, tiene", edad, "años")
# elif edad >= 18:
#     print("su nombre es: ", nombre)
#     print("su apellido es:", apellido)
#     print("su mail: ", mail)
#     print ("sos mayor de edad, tiene", edad, "años")
# else:
#     print ("gracias por ingresar los datos")

"""opcion 2 de resolucion del problema"""

"""
Para este ejercicio necesitamos un software que ayude a registrar y calcular información financiera básica para nuestros y nuestras clientes.

Tu tarea para esta semana es la siguiente:

Registrar los ingresos mensuales de un cliente durante 6 meses. Usá un bucle while para solicitar el ingreso de cada mes.Validar que los ingresos sean números positivos. Si se ingresa un valor negativo, mostrá un mensaje indicando que el valor no es válido y volvé a pedir el dato.

Calcular el total acumulado durante los 6 meses. Mostrá este resultado al final del programa.

El programa debe mostrar el apellido, nombre y dirección de correo con el formato pedido, y el texto correspondiente a su rango etario.

¡Estoy segura de que harás un excelente trabajo!

Saludos, Mariana

"""
print("bienvenido, a continuacion se pedira que ingrese su pago mensual de sus ultimos 6 meses")

contador = 1
ingreso = 0
suma = 0

while (ingreso <= 0 or contador <= 6):
    ingreso = float(input(f"ingrese su ingreso {contador}:"))
    if (ingreso < 0):
        print("ERROR: ingreso un numero negativo vuelva a ingresar otro numero")
    else:
        contador = contador + 1
        suma = suma + ingreso    
print("su ingreso total de los 6 meses es: ", suma)

print("------------------------------------------------------------------------")
print ("le pido a continuacion que ingrese sus datos personales:")

nombre = ""
apellido = ""
mail = ""
edad = 0

nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
mail = input("ingrese su mail: ")
edad = int(input("ingrese su edad :"))

if edad <= 18:
    print ("sos menor de edad,", edad)
    print("su nombre es: ", nombre)
    print("su apellido es:", apellido)
    print("su mail: ", mail)
    print("sos menor de edad, tiene", edad, "años")
elif edad >= 18:
    print("su nombre es: ", nombre)
    print("su apellido es:", apellido)
    print("su mail: ", mail)
    print ("sos mayor de edad, tiene", edad, "años")
else:
    print ("gracias por ingresar los datos")
    
print("----------------------------------------------------------")
print("los datos ingresado son:")
print("su nombre es: ", nombre)
print("su apellido es:", apellido)
print("su mail: ", mail)
print("sos mayor de edad, tiene", edad, "años")
