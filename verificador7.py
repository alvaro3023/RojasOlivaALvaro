print("CALCULADORA N°7")
#El programa calculara el perimetro de un triangulo

#INPUT
lado_a =int(input("el lado a es:"))
lado_b =int(input("el lado b es:"))
lado_c =int(input("el lado c es:"))

#PROCESSING
perimetro = lado_a + lado_b + lado_c

#VERIFICADOR
perimetro_verificado = (perimetro == 200)

#OUTPUT
print("El valor del lado a es: " + str(lado_a))
print("El valor del lado b es: " + str(lado_b))
print("El valor del lado c es: " + str(lado_c))
print("El perimetro de un triangulo es: " + str(perimetro))
print("El perimetro hallado es: " + str(perimetro_verificado))
