print("EJERCICIO N°20")
#Este programa calculara la superficie un cilindro

#INPUT
pi=float(input("el valor de pi es: "))
radio_base=int(input("el valor del radio de la base es: "))
altura_cilindro=int(input("el valor de la altura del cilindro es: "))

#PROCESSING
Superficie_cilindro=2*pi*radio_base*altura_cilindro

#VERIFICADOR
Superficie_cilindro_verificado =(Superficie_cilindro < 100)

#OUTPUT
print("El pi es: " + str(pi))
print("El radio es: " + str(radio_base))
print("La altura es: " + str(altura_cilindro))
print("La superficie de un cilindro es: " + str(Superficie_cilindro))
print("La superficie de un cilindro es menor que 100?: " + str(Superficie_cilindro_verificado))
