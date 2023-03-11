opcion = 1
empanadas = []
contId = 1
while opcion != 0:
    print("1: Ingrese una empanada: ")
    print("2: Mostrar las empanadas registradas: ")
    print("3: Buscar empanada por ID: ")
    print("4: Editar una empanada por ID: ")
    print("5: Eliminar una empanada por ID: ")
    print("0: Salir: ")
    opcion = int(input("Escoja una opción: "))
    if(opcion == 1):
        empanada = {}
        empanada["id"] = contId#int(input("Id Empanada: "))
        empanada["nombre"] = input("Nombre Empanada: ")
        empanada["precio"] = float(input("Precio Empanada: "))
        empanada["popularidad"] = int(input("Popularidad Empanada: "))
        empanada["fechaVencimiento"] = input("Fecha de Vencimiento Empanada: ")
        empanadas.append(empanada)
        print("Empanada registrada...")
        contId = contId + 1
    elif(opcion == 2):
        for empanada in empanadas:
            print(empanada)
    elif(opcion == 3):
        buscarEmpanada = int(input("Digite el ID para buscar la empanada: "))
        for empanada in empanadas:
            if(buscarEmpanada == empanada["id"]):
                print("Los datos de la empanada son: ")
                print("Id: ",empanada["id"])
                print("Nombre: ",empanada["nombre"])
                print("Precio: ",empanada["precio"])
                print("Popularidad: ",empanada["popularidad"])
                print("fechaVencimiento: ",empanada["fechaVencimiento"])
            else: print("La empanada no existe!...")
    elif(opcion == 4):
        buscarEmpanada = int(input("Digite el ID para buscar la empanada: "))
        for empanada in empanadas:
            if(buscarEmpanada == empanada["id"]):
                print("El precio actual es: ",empanada["precio"])
                empanada["precio"] = float(input("Digite el nuevo precio: "))
                print("El precio nuevo del producto " , empanada["id"]  , "es: " , empanada["precio"])
            else: print("La empanada no existe!...")
    elif(opcion == 5):
        buscarEmpanada = int(input("Digite el ID para buscar la empanada: "))
        for empanada in empanadas:
            if(buscarEmpanada == empanada["id"]):
                   empanada["id"] = ""
                   empanada["nombre"] = ""
                   empanada["precio"] = "" 
                   empanada["fechaVencimiento"] = ""
            else: print("La empanada no existe!...")
    elif(opcion == 0):
        pass
    else: print("La opcion ingresada no es valida")
    


