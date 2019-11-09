print("CALCULADORA N°6")
#E programa hallara el area del rombo a base sus diagonales y angulo

#INPUT
d1 =int(input("la d1 es:"))
d2 =int(input("la d2 es:"))
angulo=float(input("el angulo es:"))

#PROCESSING
area= 1/2* d1*d2*angulo

#VERIFICADOR
area_verificada = (area > 100)

#OUTPUT
print("El valor de la diagonal 1 es: " + str(d1))
print("El valor de la diagonal 2 es: " + str(d2))
print("El valor del angulo es:" + str(angulo))
print("El area del rombo es: " + str(area))
print("El area del rombo hallada es: " + str(area_verificada))
