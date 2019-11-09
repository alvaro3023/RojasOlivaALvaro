print("EJERCICIO N°18")
#Este programa hallara la Fuerza de rozamiento

#INPUT
u=float(input("el valor de U es: "))
N =int(input("el valor de N es "))

#PROCESSING
Fuerza_rozamiento=u*N

#VERIFICADOR
Fuerza_rozamiento_verificado = (Fuerza_rozamiento < 100)

#OUTPUT
print("Al determinar la fuerza de rozamiento multiplicamos el coeficiente de rozamiento " + str(u)
      + " con la normal " + str(N) + " resulta " + str(Fuerza_rozamiento))
print("La fuerza de rozamiento verificado es menor  que 100?: " + str(Fuerza_rozamiento_verificado))
