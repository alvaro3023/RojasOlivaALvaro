print("EJERCICIO N°11")
#El programa determinara cuanto tiempo tardara un automovil en alcanzar una velocidad de 60 km/h si parte de repospo

#INPUT
V_f=float(input("La vf es:"))
V_i=float(input("la vi es:"))
aceleracion =float(input("la aceleracion es:"))

#PROCESSING
tiempo = (V_f + V_i)/ aceleracion

#VERIFICADO
tiempo_verificado=(tiempo > 150)

#OUTPUT
print("La velocidad inicial es: " + str(V_i))
print("La velocidad final es: " + str(V_f))
print("La aceleracion es: " + str(aceleracion))
print("El tiempo que tardara el automovil es: " + str(tiempo))
print("El tiempo hallado es mayor que 150?: " + str(tiempo_verificado))
