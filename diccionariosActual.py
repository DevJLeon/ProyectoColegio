import time
import from funciones.py

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