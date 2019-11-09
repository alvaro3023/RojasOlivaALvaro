print("EJERCICIO N°1")
#este programa calculara el volumen de una esfera
#INPUT
pi=float(input("ingrese el valor de pi: "))
radio=int(input("ingrese el valor del radio: "))
angulo=float(input("ingrese el valor angulo: "))
#PROCESSING
volumen =4/3*pi*(radio**3)*angulo

#VERIFICADOR
volumen_verificado = (volumen >= 200 )

#OUTPUT
print("pi es: " + str(pi))
print("El radio es: " + str(radio))
print("El angulo es:" + str(angulo))
print("El volumen de la esfera es: " + str(volumen))
print("El volumen hallado es mayor o igual a 200?:  " + str(volumen_verificado))
