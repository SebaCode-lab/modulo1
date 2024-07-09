###El algoritmo utilizado para calcular el digito verificador en el siguiente
###Se toman todos los números del RUT (sin el dígito verificador). 12884419
###Se da vuelta esa cifra, es decir, reordenamos los números comenzando de derecha a izquierda. 91448821
###Se da vuelta esa cifra, es decir, reordenamos los números comenzando de derecha a izquierda. Quedaría 91448821
###Se Multiplican cada uno de estos números por la siguiente serie: 2, 3, 4, 5, 6, 7 y si se acaba la serie, se vuelve  a empezar 2, 3, 4…
###9 × 2 = 18
###1 × 3 = 3
###4 × 4 = 16
###4 × 5 = 20
###8 × 6 = 48
###8 × 7 = 56
###2 × 2 = 4
###1 × 3 = 3
###Una vez hecho esto, se suman todos los resultados:
###18 +3 +16 +20 +48 +56 +4 +3 =168
###El resultado obtenido se dividimos por 11, para luego obtener el resto de esa división
###168 /11 =15.27272727272727
###Tomamos el resultado sin decimales y sin aproximación. En este caso quedaría 15 y lo multiplicamos por 11 (15x11 =165)
###Posteriormente, al resultado de la suma de los produtos (ver linea 14) se le resta el resulato  obtentido en la linea 17 (168-165=3)
###Al Resultado enterior le restamos 11 le restamos el resultado anterior (11-3=8)
###El resultado de esta sustracion corresponde al digito verificador del RUT en chile, en este caso el digito verificador del RUT 12884419 es 8
###Si como resultado final del calculo del digito verificador es 11 el digito verificador sera 0 y si es 10 sera la tera K
### 11 =>0
### 10 =>K

rut=input("Ingrese el RUT sin digito verificador: ")

#Operacion matematica:
num1=int(rut[0])*3
num2=int(rut[1])*2
num3=int(rut[2])*7
num4=int(rut[3])*6
num5=int(rut[4])*5
num6=int(rut[5])*4
num7=int(rut[6])*3
num8=int(rut[7])*2

suma= num1+num2+num3+num4+num5+num6+num7+num8

division=suma % 11

digitoverificador= 11 - division

if digitoverificador==10:
    digitoverificador="k"
elif digitoverificador==11:
    digitoverificador="0"
else:digitoverificador=digitoverificador
if digitoverificador==10:
    digitoverificador="k"
elif digitoverificador==11:
    digitoverificador="0"
else:digitoverificador=digitoverificador

print ("Su rut es: ", str(rut)+"-"+str(digitoverificador))            








