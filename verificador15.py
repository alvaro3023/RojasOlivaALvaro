print("CALCULADORA N°15 ")
#Este programa hallara el trabajo realizado por un auto

#INPUT
masa=float(input("la masa es: "))
aceleracion=int(input("la acelaracion es: "))
distancia=float(input("la distancia es: "))

#PROCESSING
fuerza=masa*aceleracion
trabajo=fuerza*distancia

#VERIFICADOR
trabajo_verificado =(trabajo < 150)

#OUTPUT
print("La masa es: " + str(masa))
print("La aceleracion es: " + str(aceleracion))
print("La distancia es: " + str(distancia))
print("La fuerza es: " + str(fuerza))
print("El trabajo es: " + str(trabajo))
print("El trabajo verificado es menor que 150?: " + str(trabajo_verificado))
