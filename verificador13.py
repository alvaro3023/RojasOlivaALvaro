print("EJERCICIO N°13 ")
#Este programa hallara el Tiempo de encuentro

#INPUT
V_a=float(input("la veloc. a es: "))
V_b=float(input("la veloc. b es: "))
distancia=int(input("la distancia es: "))

#PROCESSING
tiempo_encuentro= d/(Va-Vb)

#VERIFICADOR
tiempo_encuentro_verificado=(tiempo_encuentro <200)

#output
print("La velocidad a es: " + str(V_a))
print("La velocidad b es: " + str(V_b))
print("La distancia es: " + str(distancia))
print("El tiempo de encuentro es: " + str(tiempo_encuentro))
print("El tiempo de encuentro hallado es menor que 200?: " + str(tiempo_encuentro_verificado))
