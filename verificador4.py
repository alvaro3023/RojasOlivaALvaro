print("EJEMPLO N°4")
#el programa calculara el area de un trapecio
#INPUT
base_mayor =int(input("la base mayor es:"))
base_menor =int(input("la base menor es:"))
altura =float(input("la altura es:"))

#processing
area_trapecio = (base_mayor + base_menor )/2*altura

#VERIFICADOR
area_trapecio_verificado = (area_trapecio == 100)

#OUTPUT
print("La base mayor de un trapecio es: " + str(base_mayor))
print("La base menor de un trapecio es: " + str(base_menor))
print("El area del trapecio es: " + str(area_trapecio))
print("El area del trapecio hallado es: " + str(area_trapecio_verificado))
