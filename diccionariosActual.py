import time

time.sleep()

##MUY IMPORTANTE: cuando no haya nota, esta tendrà el valor "P" de Pendiente :)
## RULES** 1. NOTAS, ESTUDIANTES , MATERIAS 2. Todos los estudiantes deben estar inscritos en las materias (todos los diccionarios deben estar vacìos(inicio)) *OPTIONAL: si elimino estudiante, se le borraràn todas las notas. Si borro la materia, no se puede si tiene notas asociadas* 3. no registrar 3 notas al tiempo 4. n2 solo si todos tienen n1 y lo mismo con n3(tienen n2) 5. Despues de registrar n1 no se admitiràn màs estudiantes en la materia, 6. Luego de registrar NF(n3) no se pueden modificar las notas  // cambiar crearnota por inscribir estudiantes a la materia


optMenu = 1
#############################################         DICCIONARIOS       ##################################################################################################

dicEstudiantes = {
    1:{
    "nombres":"Juan Gavioto",
    "apellidos":"Gonzales Mora",
    "correo":"jgavmora@gmail.com"
    },
    2:{
    "nombres":"Daniela",
    "apellidos":"Estupinhan Garcia",
    "correo":"jgavmora@gmail.com"
    },
    3:{
    "nombres":"Santiago",
    "apellidos":"Lopez Aguilar",
    "correo":"jgavmora@gmail.com"
    },
    4:{
    "nombres":"Jonathan",
    "apellidos":"Maldonado Gutierrez",
    "correo":"jgavmora@gmail.com"
    },
    5:{
    "nombres":"Milthon",
    "apellidos":"Lopez Obrador",
    "correo":"jgavmora@gmail.com"
    },
    6:{
    "nombres":"Santiago",
    "apellidos":"Peña Nieto",
    "correo":"jgavmora@gmail.com"
    },
}

dicMaterias = {
    1:{"nomMateria":"Matematicas"},
    2:{"nomMateria":"Biologia"},
    3:{"nomMateria":"Fisica"},
    4:{"nomMateria":"Quimica"},
    5:{"nomMateria":"GeoFisica"}
}

dicNotas ={
    1:{"idEstudiante":1,
       "idMateria":3,
       "nota1":4.5,
       "nota2":5,
       "nota3":5,
       "notaFinal":4.9
       },
       2:{"idEstudiante":3,
       "idMateria":3,
       "nota1":4.5,
       "nota2":5,
       "nota3":5,
       "notaFinal":4.9}
}

###########################################          FUNCIONES NOTAS          ######################################################################################
#
def agregarNotas(diccionario, idEstudiante, idMateria):
    n1= float(input("Ingrese la primera nota"))
    n2="P"
    n3="P"
    nF="P"
    id = crearId(diccionario)
        
    diccionario[id+1] = {
        "idEstudiante":idEstudiante,
        "idMateria":idMateria,
        "nota1":n1,
        "nota2":n2,
        "nota3":n3,
        "notaFinal":nF,
        }
    ingresar = int(input("?Desea Ingresar la siguiente nota?: 1.SI 2.NO \t"))
    if ingresar == True:
        n2 = float(input("Ingrese la segunda nota"))
        if ingresar == True:
            ingresar = int(input("?Desea Ingresar la siguiente nota?: 1.SI 2.NO \t"))
            if ingresar == True:
                n3 = float(input("Ingrese la tercera nota"))
                nF= ((n1+n2+n3)/3)

    diccionario[id+1] = {
        "idEstudiante":idEstudiante,
        "idMateria":idMateria,
        "nota1":n1,
        "nota2":n2,
        "nota3":n3,
        "notaFinal":nF,
        }
    
    return diccionario

def verNotas(diccionario):
    listaNotas = "ID \t Nom. Est \t ASIGNATURA \t nota1 \t nota2 \t nota3 \t notaFINAL\n\n"

    for idNota in diccionario:
        idEstud = diccionario[idNota]["idEstudiante"]
        idMat = diccionario[idNota]["idMateria"]
        listaNotas += (str(idNota) + " \t" + str(dicEstudiantes[diccionario[idNota]["idEstudiante"]]["nombres"])+ " \t" +str(dicMaterias[idMat]["nomMateria"])+ " \t" + str(diccionario[idNota]["nota1"])+ " \t" + str(diccionario[idNota]["nota2"])+ " \t" + str(diccionario[idNota]["nota3"])+ " \t" + str(diccionario[idNota]["notaFinal"]) +"\n")
    return print(listaNotas)

def verNota():
    nota = None

def editarNotas(diccionario, id, key):
    
    if key == 1:
        key = "nota1"
        cambio = float(input("Ingrese la nueva primera nota: \t"))
        print("*******Nota 1 cambiada satisfactoriamente ************")
    elif key == 2:
        key = "nota2"
        cambio = float(input("Ingrese la nueva segunda nota: \t"))
        print("*******Nota 2 cambiada satisfactoriamente ************")
    elif key == 3:
        key = "nota3"
        cambio = float(input("Ingrese la nueva tercera nota: \t"))
        print("\n*******Nota 3 cambiada satisfactoriamente ************\n")
    
    diccionario[id][key] = cambio
    if diccionario[id]["nota3"] != "P":
        calcularDefinitiva(id)

    verNotas(diccionario)

def calcularDefinitiva (id):
    n1 = dicNotas[id]["nota1"]
    n2 = dicNotas[id]["nota2"]
    n3 = dicNotas[id]["nota3"]
    dicNotas[id]["notaFinal"] = (n1+n2+n3)/3

#############################################       FUNCIONES MATERIAS    ##################################################################################################

def crearId(diccionario):
    id = list(diccionario.keys())[len(diccionario)-1]
    return id

def agregarMateria(materia, nombreMateria):
    id = crearId(materia)
    materia[id+1] = {"nomMateria":nombreMateria}
    return materia

def verMaterias(materias):
    listaMaterias = ""
    for materia in materias:
        listaMaterias += str(materia) + " " + str(materias[materia]["nomMateria"]+"\n")
    return listaMaterias

def editarMateria(diccionario, id, newName):
    diccionario[id] = {"nomMateria": newName}

###########################################          FUNCIONES ESTUDIANTES          ######################################################################################

def agregarEstudiante(diccionario, nombreEstudiante, apellidoEstudiante, correo):
    id = crearId(diccionario)

    diccionario[id+1] = {
        "nombres":nombreEstudiante,
        "apellidos":apellidoEstudiante,
        "correo":correo
        }
    return diccionario

def verEstudiantes(diccionario):
    listaEstudiantes = ""
    for estudiante in diccionario:
        listaEstudiantes += (str(estudiante) + " \t" + str(diccionario[estudiante]["nombres"]) + " \t" + str(diccionario[estudiante]["apellidos"]) + " \t" + str(diccionario[estudiante]["correo"]) + "\n")
    return print(listaEstudiantes)

def editarEstudiante(diccionario, id, key,cambio):
    diccionario[id][key] = cambio

def delete(diccionario):
        codigo = int(input("Ingrese el codigo de la ID a elminiar: \t"))
        del(diccionario[codigo])
#############################################            MENUS            ##################################################################################################

def menuMaterias(materias):
    print("*********************************************MATERIAS**************************************************************")
    opcion = int(input("\n\nSeleccione alguna de las siguientes opciones:\n1.Agregar \t 2.Editar\n3.Eliminar \t 0.Volver\n"))

    if opcion == 1:
        nomMateria = input("Ingrese el nombre de la materia: \t")
        agregarMateria(materias,nomMateria)
    elif opcion == 2:
        editarMateria(materias,int(input("Ingrese el ID de la materia a editar: \t")),input("Indique el nuevo nombre de la materia"))
        print("\n***MATERIA EDITADA CON ÈXITO***")
    elif opcion == 3:
        codigo = int(input("Ingrese el codigo de la materia a elminiar: \t"))
        del(dicMaterias[codigo])
    elif opcion == 0:
        print(verMaterias(dicMaterias))

def menuEstudiantes(diccionario):
    continueEdit = 1
    print("*********************************************MATERIAS**************************************************************")
    opcion = int(input("\n\nSeleccione alguna de las siguientes opciones:\n1.Agregar \t 2.Editar\n3.Eliminar \t 0.Volver\n"))

    if opcion == 1:
        nombre = input("Ingrese el nombre del estudiante: \t")
        apellido = input("Ingrese el apellido del estudiante: \t")
        correo = input("Ingrese el correo del estudiante: \t")
        agregarEstudiante(diccionario,nombre,apellido,correo)
        print("****************************ESTUDIANTE AGREGADO CON EXITO********************************")
        time.sleep(2)
        verEstudiantes(diccionario)
    elif opcion == 2:
        while continueEdit == True:
            cambio = ""
            verEstudiantes(diccionario)
            IDestudiante = int(input("Indique el ID del estudiante a editar: \t"))
            key = int(input("Indique que desea editar del estudiante: \n1.Nombres \t2.Apellidos \n3.Correo: \t"))
            if key == 1:
                key = "nombres"
                cambio = input("Inserte nombre(s) modificado: \t")
            elif key == 2:
                key = "apellidos"
                cambio = input("Inserte apellido(s) modificado: \t")
            elif key == 3:
                key = "correo"
                cambio = input("Inserte correo(s) modificado: \t")
            editarEstudiante(diccionario,IDestudiante,key,cambio)
            continueEdit = int(input("?Desea continuar?"))
    elif opcion == 3:
        verEstudiantes(diccionario)
        delete(diccionario)
    elif opcion == 0:
        verEstudiantes(diccionario)

def menuNotas(diccionario):
    print("*********************************************NOTAS**************************************************************")
    opcion = int(input("\n\nSeleccione alguna de las siguientes opciones:\n1.Agregar \t 2.Editar\n3.Eliminar \t 0.Volver\n"))

    if opcion == 1:
        verEstudiantes(dicEstudiantes)
        idAlumno = int(input("Ingrese el ID del alumno: "))
        verMaterias(dicMaterias)
        idMateria = int(input("Ingrese el ID de la materia: "))
        agregarNotas(diccionario,idAlumno,idMateria)
        print("****************************NOTA AGREGADA CON EXITO********************************")
        verNotas(diccionario)
    elif opcion == 2:
            verNotas(dicNotas)
            id = int(input("Ingrese el ID de la nota: \t"))
            key = int(input("Seleccione la nota a editar: 1. Nota1 2.Nota2 3.Nota3"))
            editarNotas(diccionario,id,key)
    elif opcion == 3:
        verNotas(diccionario)
        delete(diccionario)
    elif opcion == 0:
        None

#############################################          ACCIONES           ##################################################################################################

while optMenu != 0:
    optMenu = int(input("\n\nSeleccione alguna de las siguientes opciones:\n1.Notas \t 2.Estudiantes\n3.Materias \t 0.Salir\n"))
    if optMenu == 1:
        menuNotas(dicNotas)
    elif optMenu == 2:
        menuEstudiantes(dicEstudiantes)
    elif optMenu == 3:
        menuMaterias(dicMaterias)
    else :
        print("Adios, cv")    


#************************************************PRUEBAS************************************************
#print((len(dicEstudiantes[1].keys())))
#verNotas(dicNotas)
#print(verEstudiantes(dicEstudiantes))
#agregarMateria(dicMaterias,"Artes")
#print(dicMaterias)
##print(verMaterias(dicMaterias))