print("EJERCICIO N°8")
#Este programa calculara la Tasa de natalidad

#INPUT
nac_hombres=int(input("los hombres nacidos son:"))
nac_mujeres=int(input("las mujeres nacidas son:"))
pob_total =int(input("la poblacion total es:"))

#PROCESSING
tasa_natalidad = ((nac_hombres + nac_mujeres)/pob_total)*100

#VERIFICADO
tasa_natalidad_verificado =(tasa_natalidad < 300)

#OUTPUT
print("El numero de hombres nacidos: " + str(nac_hombres))
print("el numero de mujeres nacidas " + str(nac_mujeres))
print("La poblacion total: " + str(pob_total))
print("La Tasa de Natalidad es: " + str(tasa_natalidad))
print("La tasa de natalidad hallada es: " + str(tasa_natalidad_verificado))
