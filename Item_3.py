"""Supón que un ramo tiene las siguientes evaluaciones:
 3 tareas en Laboratorio, estas valen un 15% del curso,
 3 tareas en clase, que valen un 15% del curso, y Elabora un programa que, ingresando todas las notas, entregue la nota de presentación."""

#Ingreso de datos de las 3 notas de Laboratorio:
lab1=float (input("Ingrese la nota de la tarea 1 de laboratorio: "))
lab2=float (input("Ingrese la nota de la tarea 2 de laboratorio: "))
lab3=float (input("Ingrese la nota de la tarea 3 de laboratorio: "))

#Calculo de las notas de las 3 tareas de laboratorio:
PromemedioLab=(lab1+lab2+lab3)/3

print("Su promedio de notas de las tareas de laboratorio es: ")
print(round(PromemedioLab, 1))

#Ingreso de datos de las notas de los tareas en clases:
Tarea1=float (input("Ingrese la nota de la tarea en clases N°1: "))
Tarea2=float (input("Ingrese la nota de la tarea en clases N°2: "))
Tarea3=float (input("Ingrese la nota de la tarea en clases N°3: "))

#Calculo de las notas de las 3 tareas en Clases:
PromedioTareas=(Tarea1+Tarea2+Tarea3)/3

print("Su promedio de notas de las tareas de laboratorio es:")
print(round(PromedioTareas, 1))

#Ingreso de datos de las notas de las 2 pruebas solemnes:
Sole1=float (input("Ingrese la nota de la prueba solemne N°1: "))
Sole2=float (input("Ingrese la nota de la prueba solemne N°2: "))

#Calculo del promedio de las notas solemnes:
PromedioSole=(Sole1+Sole2)/2

#Calculo del porcentaje de las tareas:
NotaPresentacion=(PromemedioLab)*0.15+(PromedioTareas)*0.15+Sole1*0.35+Sole2*0.35

#Entrega de Nota de presentacion a examen:
print("Su nota de presentacion al examen es:")
print(round(NotaPresentacion ,1))



