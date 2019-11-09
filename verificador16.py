print("EJERCICIO N°16")
#Este programa calculara la energia cinetica de un X cuerpo

#INPUT
masa=float(input("la masa es: "))
velocidad_1=float(input("la velocidad 1 es: "))
velocidad_2=float(input("la velicidad 2 es:"))

#PROCESSING
Ec= (masa*velocidad_1 * velocidad_2)/2

#VERIFICADOR
Ec_verificado =(Ec >= 200)

#OUTPUT
print("La masa de la energia es: " + str(masa))
print("La velocidad 1 es: " + str(velocidad_1))
print("la velocidad 2 es: " + str(velocidad_2))
print("La energia cinetica es: " + str(Ec))
print("La energia cinetica hallada es mayor o igual que 200?: " + str(Ec_verificado))
