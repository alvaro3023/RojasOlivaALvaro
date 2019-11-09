print("EJERCICIO N°14 ")
#Este programa hallara la densidad de un liquido X

#INPUT
masa=float(input("la masa es: "))
velocidad=int(input("la velocidad es: "))
volumen=float(input("el volumen es: "))
#calcular
densidad =(masa/velocidad)*volumen

#VERIFICADOR
densidad_verificado =(densidad == 100)

#OUTPUT
print("EL valor de la masa es: " + str(masa))
print("El valor de la velocidad es: " + str(velocidad))
print("El valor de la densidad es: " + str(densidad))
print("La densidad hallado es igual a 100?: " + str(densidad_verificado))
