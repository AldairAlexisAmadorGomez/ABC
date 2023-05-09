pacientes = {}  # Diccionario para almacenar la información de los pacientes

#La función cargar_pacientes recibe un nombre de archivo como parámetro y se encarga de cargar la información
#de los pacientes desde ese archivo. Abre el archivo en modo lectura, lee todas las líneas y recorre cada línea.
#Cada línea se divide en valores separados por comas y se asignan a las variables 
#correspondientes (nombre, edad, género, especie, estado). Luego se agrega un nuevo elemento al diccionario pacientes 
#con el nombre como clave y un diccionario con los detalles del paciente como valor. Finalmente, 
#se llama a la función guardar_paciente para guardar las líneas del archivo en un nuevo archivo llamado "pacientes.txt".
def cargar_pacientes(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                paciente = linea.strip().split(",")
                nombre = paciente[0]
                edad = paciente[1]
                genero = paciente[2]
                especie = paciente[3]
                estado = paciente[4]
                pacientes[nombre] = {"Edad": edad,
                                     "Género": genero, "Especie": especie, "Estado": estado}
        print("Carga de pacientes exitosa.")
        guardar_paciente(lineas, "pacientes.txt")
    except FileNotFoundError:
        print("El archivo no existe.")

#La función guardar_paciente recibe como parámetros una lista de líneas correspondientes a la información de un paciente
#y el nombre del archivo en el que se desea guardar. Abre el archivo en modo añadir (si el archivo no existe, se crea) 
#y escribe las líneas en el archivo.
#Esta función se utiliza para guardar la información de un nuevo paciente en el archivo "pacientes.txt".
def guardar_paciente(paciente, nombre_archivo):
    with open(nombre_archivo, "a") as archivo:
        archivo.writelines(paciente)
    print("Paciente guardado en el archivo.")

#Se inicia un ciclo while que se ejecuta indefinidamente hasta que se elija la opción "5" para salir.
while True:
    # Mostrar las opciones disponibles
    print("Opciones:")
    print("1. Registro de pacientes")
    print("2. Lista de espera")
    print("3. Listado de medicamentos")
    print("4. Recomendaciones")
    print("5. Salir")
    opcion = input("Ingrese la opción deseada: ")

    # Ejecutar la opción seleccionada

    #Si se selecciona la opción "1" (Registro de pacientes), se muestra un submenú con las opciones "A" y "B". "A" 
    #permite cargar pacientes desde un archivo y "B" permite ingresar los datos de un nuevo paciente manualmente.
    #Según la subopción seleccionada, se llama a las funciones cargar_pacientes o guardar_paciente para cargar 
    #los pacientes desde un archivo o ingresar un nuevo paciente, respectivamente.
    if opcion == "1":
        print("1. Volver Al Menú Anterior")
        print("A. Carga masiva de pacientes desde archivo")
        print("B. Ingresar nuevo paciente")
        subopcion = input("Ingrese la subopción deseada: ")

        if subopcion == "A":
            nombre_archivo = input("Ingrese el nombre del archivo: ")
            cargar_pacientes(nombre_archivo)
        elif subopcion == "B":
            nombre = input("Ingrese el nombre del paciente: ")
            edad = input("Ingrese la edad del paciente: ")
            genero = input("Ingrese el género del paciente: ")
            especie = input("Ingrese la especie del paciente: ")
            estado = input("Ingrese el estado del paciente: ")

            pacientes[nombre] = {"Edad": edad,
                                 "Género": genero, "Especie": especie, "Estado": estado}
            paciente_str = f"{nombre},{edad},{genero},{especie},{estado}"
            guardar_paciente(paciente_str, "pacientes.txt")
        else:
            print("Opción inválida. Intente nuevamente.\n")

    #Si se selecciona la opción "2" (Lista de espera), se muestra un submenú con las opciones de visualización: 
    #"A" para mostrar todos los pacientes registrados, 
    #"B" para mostrar los pacientes en proceso de operación y 
    #"C" para mostrar los pacientes en postoperatorio. Dependiendo de la subopción seleccionada, 
    #se recorre el diccionario de pacientes y se imprimen los detalles 
    #de los pacientes que cumplen con el estado especificado.
    elif opcion == "2":
        print("Opciones de visualización:")
        print("A. Todos los pacientes registrados")
        print("B. Pacientes en proceso de operación")
        print("C. Pacientes en postoperatorio")
        subopcion = input("Ingrese la subopción deseada: ")

    if subopcion == "A":
        print("Lista de pacientes registrados:")
        for nombre, detalles in pacientes.items():
            print("Nombre:", nombre)
            print("Edad:", detalles["Edad"])
            print("Género:", detalles["Género"])
            print("Especie:", detalles["Especie"])
            print("Estado:", detalles["Estado"])
            print()  # Línea en blanco para separar los pacientes

    elif subopcion == "B":
        print("Pacientes en proceso de operación:")
        for nombre, detalles in pacientes.items():
            if detalles["Estado"] == "En proceso de Operacion":
                print("Nombre:", nombre)
                print("Edad:", detalles["Edad"])
                print("Género:", detalles["Género"])
                print("Especie:", detalles["Especie"])
                print("Estado:", detalles["Estado"])
                print()  # Línea en blanco para separar los pacientes

    elif subopcion == "C":
        print("Pacientes en postoperatorio:")
        for nombre, detalles in pacientes.items():
            if detalles["Estado"] == "PostOperatorio":
                print("Nombre:", nombre)
                print("Edad:", detalles["Edad"])
                print("Género:", detalles["Género"])
                print("Especie:", detalles["Especie"])
                print("Estado:", detalles["Estado"])
                print()  # Línea en blanco para separar los pacientes    

    #Si se selecciona la opción "3" (Listado de medicamentos), se solicita al usuario que ingrese el nombre del paciente.
    #Se verifica si el paciente está registrado en el diccionario pacientes y, de ser así, 
    #se busca si tiene medicamentos registrados. En caso afirmativo, se imprimen los medicamentos necesarios para el posoperatorio.
    #Si no se encuentran medicamentos registrados, se muestra un mensaje indicando
    #Que no se encontraron medicamentos para el paciente.
    elif opcion == "3":
        print("Listado de medicamentos:")
        nombre_paciente = input("Ingrese el nombre del paciente: ")
        if nombre_paciente in pacientes:
            detalles = pacientes[nombre_paciente]
            if "Medicamentos" in detalles:
                medicamentos = detalles["Medicamentos"]
                if medicamentos:
                    print("Medicamentos necesarios para el posoperatorio:")
                    for medicamento in medicamentos:
                        print("- ", medicamento)
                else:
                    print(
                        "No se encontraron medicamentos registrados para el paciente.")
            else:
                print("No se encontraron medicamentos registrados para el paciente.")
        else:
            print("El paciente no se encuentra registrado.")

    #Si se selecciona la opción "4" (Recomendaciones), se solicita al usuario que ingrese el nombre del paciente.
    #Se verifica si el paciente está registrado en el diccionario pacientes y, de ser así,
    #se obtiene la especie y el género del paciente. Dependiendo de la especie y el género,
    #se imprimen las recomendaciones específicas para ese tipo de paciente. Si se trata de un gato macho, se imprimen las recomendaciones correspondientes. 
    #Si es una gata hembra, se imprimen otras recomendaciones. Para perros machos y hembras, 
    #también se imprimen recomendaciones diferentes. Si no se encuentra ninguna recomendación específica para el género y 
    #especie del paciente, se muestra un mensaje indicando que no se encontraron recomendaciones.
    elif opcion == "4":
        print("Recomendaciones")
        nombre_paciente = input("Ingrese el nombre del paciente: ")            
        if nombre_paciente in pacientes:
            detalles = pacientes[nombre_paciente]
            especie = detalles["Especie"]
            genero = detalles["Género"]

            if especie == "gato":
                if genero == "macho":
                    print("Recomendaciones para gato macho:")
                    print("- Descansar 3 horas")
                    print("- Mantenerse hidratado")
                    print("- Revisar la herida una o dos veces al día")
                elif genero == "hembra":
                    print("Recomendaciones para gato hembra:")
                    print("- Descansar 5 horas")
                    print("- Mantenerse hidratada")
                    print("- Uso de collar isabelino")
                else:
                    print("No se encontraron recomendaciones para este género de gato.")
            elif especie == "perro":
                if genero == "macho":
                    print("Recomendaciones para perro macho:")
                    print("- Descansar 3 horas")
                    print("- Mantenerse hidratado")
                    print("- Revisar la herida una o dos veces al día")
                elif genero == "hembra":
                    print("Recomendaciones para perro hembra:")
                    print("- Descansar 5 horas")
                    print("- Mantenerse hidratada")
                    print("- Administrar la medicación")
                else:
                    print("No se encontraron recomendaciones para este género de perro.")
            else:
                print("No se encontraron recomendaciones para esta especie.")
        else:
            print("El paciente no se encuentra registrado.")
    #Salir del programa
    elif opcion == "5":
        print("Se terminó el programa")
        break
    #Si se ingresa una opción inválida en cualquier momento, 
    #se muestra un mensaje de error y se vuelve al principio del ciclo while
    #para solicitar nuevamente una opción válida. 
    else:
        print("Opción inválida. Intente nuevamente.\n")