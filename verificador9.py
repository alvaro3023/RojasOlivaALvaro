print("EJERCICIO N°9")
#Este programa calculara la Tasa de mortalidad

#INPUT
muerte_provocada=int(input("Las muertes provocadas son: "))
muerte_natural=int(input("Las muertes naturales son:"))
pob_total =int(input("La poblacion total son: "))

#PROCESSING
tasa_mortalidad =(muerte_provocada + muerte_natural)/pobTotal * 100

#VERIFICADOR
tasa_mortalidad_verificado = (tasa_mortalidad <= 300)

#OUTPUT
print("Las muertes provocadas son: " + str(muerte_provocada))
print("Las muertes naturales son: " + str(muerte_natural))
print("La poblacion total es: " + str(pob_total))
print("La tasa de mortalidad es: " + str(tasa_mortalidad) + "%")
print("La tasa de mortalidad hallado es: " + str(tasa_mortalidad_verificado))
