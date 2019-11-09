print("EJERCICIO N°19")
#Este programa calculara la potencia

#INPUT
masa=float(input("el valor de la masa es: "))
aceleracion=float(input("el valor de la aceleracion es: "))
distancia=int(input("el valor de la distancia es: "))
tiempo = float(input("el valor del tiempo es:"))

#PROCESSING
fuerza=masa*aceleracion
trabajo=fuerza*distancia
potencia = trabajo/tiempo

#VERIFICADOR
potencia_verificado =( potencia > 160)

#OUTPUT
print("La fuerza es: " + str(fuerza))
print("El trabajo es: " + str(trabajo))
print("La potencia es: " + str(potencia))
print("La potencia verificada es mayor que 160? " + str(potencia_verificado))
