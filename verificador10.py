print("EJERCICIO N°10")
#El programa determinara el tiempo en que recorre el niño de su casa hacia el colegio

#INPUT
velocidad =int(input("La velocidad es: "))
distancia = int(input("la distancia es: "))
aceleracion_1 =int(input("la aceleracion es: "))

#PROCESSING
tiempo = ((distancia / velocidad)*aceleracion_1)

#VERIFICADOR
tiempo_verificado = (tiempo == 100)

#OUTPUT
print("La velocidad es: " + str(velocidad))
print("La distancia es: " + str(distancia))
print("la aceleracion es:" + str(aceleracion_1))
print("El tiempo que recorre es: " + str(tiempo))
print("El tiempo hallado es: " + str(tiempo_verificado))
