print("EJERCICIO N°3")
#este programa calculara el area de un circulo

#INPUT
pi=float(input("el pi es:"))
radio_1=int(input("el radio n°1 es:"))
radio_2=int(input("el radio n°2 es:"))

#PROCESSING
area_circulo = pi*(radio_1*radio_2)

#VERIFICADOR
area_circulo_verificado = (area_circulo < 150)

#OUTPUT
print("El pi es: " + str(pi))
print("El radio n°1 es: " + str(radio_1))
print("El radio n°2 es: " + str(radio_2))
print("El area de un circulo es: " + str(area_circulo))
print("El area del circulo hallado es menor? " + str(area_circulo_verificado))
