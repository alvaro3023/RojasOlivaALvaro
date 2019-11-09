print("EJERCICIO N°5")
#El programa hallara el area del paralelogramo a base de dos lados y el angulo entre ellos

#INPUT
lado_1 =int(input("el lado 1 es:"))
lado_2 =int(input("el lado 2 es:"))
sen30 = float(input("el angulo es:"))

#PROCESSING
area_paralelogramo = lado_1*lado_2*sen30

#VERIFICADOR
area_paralelogramo_verificado = (area_paralelogramo < 200)

#OUTPUT
print("El valor del lado 1 es: " + str(lado_1))
print("El valor del lado 2 es: " + str(lado_2))
print("El seno de 30 es: " + str(sen30))
print("El area del paralelogramo es: " + str(area_paralelogramo))
print("EL area del paralelogramo hallado es: " + str(area_paralelogramo_verificado))
