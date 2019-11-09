print("EJERCICIO N°12 ")
#Este programa hallara el tiempo de alcance

#INPUT
V_1=float(input("la veloc.1 es: "))
V_2=float(input("la veloc.2 es: "))
distancia =int(input("la distancia es: "))

#PROCESSING
tiempo_alcance = distancia/(V_1+V_2)

#VERIFICADOR
tiempo_alcance_verificado = (tiempo_alcance != 100)

#OUTPUT
print("La velocidad 1 es: " + str(V_1))
print("La velocidad 2 es: " + str(V_2))
print("La distancia es: " + str(distancia))
print("El tiempo de alcance es: " + str(tiempo_alcance))
print("El tiempo de alcance hallado es diferente?: " + str(tiempo_alcance_verificado))
