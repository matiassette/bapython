"""
Pre proyecto:
ingreso de datos de productos: el sistema debe permitir ingresar datos basicos de los productos:nombre,categoria y precio(sin centavos).Estos datos deben almmacenrse en una lista,donde cada producto sea representado/a com sub lista de tres elementos (nombre,categoria yprecio)
visualizacion de productos registrados:El programa debe incluir una funcionalidad para mostrr en pantalla todos los productos ingresados.La informacion debe presentarse de manera ordenada y legible con cada producto numerado.
busqueda de productos:el sistema debe permitir buscar productos por su nombre.Si encunetra coincidencias, debe mostrar la infomracion completa de los productos que coincidan.Si no hay coincidencia, debe informar que no se contraron resultados.
eliminacion de productos:El sitema debe permitir eliminar un producto de la lista, identificado por su posicion (numero) de la lista


"""


print("binvenido al programa, a continuacion se brindaran una serie de opciones: ")
print("Sistema de Gestion Basica de Productos")

opcion = 0
datos = [["matias", "persona", "250"], ["sergio", "persona", "250"]]

while opcion != 5:
    # se validan datos de entrada
    print("\n1. Agregar producto: ", "\n2. Mostrar Producto: ",
        "\n3. Buscar producto: ", "\n4. Eliminar producto:", "\n5. Salir:\n")

    opcion = input("ingrese una opcion del 1 al 5: ")
    # validacion no se logro validar ya que el programa no inicia si se valida los datos
    if opcion.isnumeric():
        opcion = int(opcion)
        if opcion > 0 or opcion <= 5:
            if opcion == 1:
                # se ingresan datos de opciones con informacion a guardar en una lista de sub lista
                nombre = input("ingrese el nombre: ").capitalize()
                categoria = input("ingrese la categoria: ").capitalize()
                precio = int(input("ingrese el precio: $ "))
                datos.append([nombre, categoria, precio])
                print("se agregaron sactifactoriamente sus datos\n")
                print("sus datos ingresados son:  ", datos)
            elif opcion == 2:
                # se muestran los datos del programa
                print("")
                print("sus datos son: ")
                for indice, producto in enumerate(datos):
                    print(
                        f"{indice+1}. {producto[0]}, {producto[1]}, ${producto[2]}")
            elif opcion == 3:
                # Mostrar toda la lista
                print("Contenido de la lista: \n")
                for i in range(len(datos)):
                    print(f"Sublista {i + 1}: {datos[i]}")
                # Entrada del usuario
                entrada = input(
                    "\nIngrese el nombre a buscar: ").lower()
                encontrado = False
                # Buscar en todas las sublistas
                for i in range(len(datos)):
                    item = datos[i][0]
                    if str(item).lower() == entrada:
                        print(
                            f"\n'{entrada}' fue encontrado en la sublista {i + 1}: {datos[i]}")
                        encontrado = True
                        break  # Salta a la siguiente sublista si ya encontró coincidencia
                if not encontrado:
                    print(
                        f"\n'{entrada}' no fue encontrado en ninguna sublista.")
            elif opcion == 4:
                # Mostrar toda la lista
                print("Contenido de la lista:")
                print(("su lista es: "))
                posicion = 0
                for i in datos:
                    posicion = posicion + 1
                    print(posicion, ". ", i)
                # Entrada del usuario
                entrada = int(input(
                    "\nIngrese la posicion a eliminar: "))
                datosAxiliar = []
                for i in range(len(datos)):
                    print("que soy>>>>> ", i)
                    if i+1 != entrada:
                        datosAxiliar.append(datos[i])
                print("se elimino satisfactoriamente la lista", entrada)
                datos = datosAxiliar
                print("su lista quedo ", datos)
            elif opcion == 5:
                print("gracias por usar el programa hasta la proxima")
                break
        else:
            print("numero equivocado re intente numeros del 1 al 5")
    else:
        print("ingrese un numero del 1 al 5 ya que no ingreso nada")
        continue
