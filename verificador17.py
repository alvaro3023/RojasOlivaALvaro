print("EJERCICIO N°17")
#Este programa calculara el Peso de un cuerpo

#INPUT
masa =float(input("la valor de la masa es: "))
gravedad =int(input("el valor de la gravedad es: "))

#PROCESSING
peso = masa * gravedad

#VERIFICADOR
peso_verificado =(peso == 120)

#OUTPUT
print("el peso de un cuerpo es: " + str(peso))
print("El peso verificado es igual a 120?: " + str(peso_verificado))
