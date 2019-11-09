print("BOLETA N°10")
#INPUT
empresa=input("Nombre de la empresa: ")
fecha=input("la fecha es: ")
telefono=int(input("El numero telefonico es: "))
cliente=input("El nombre del cliente es:")
costo_toldo=int(input("El costo del toldo es: "))
costo_fondo=int(input("El costo del fondo es: "))
costo_mesas=int(input("El costo de las mesas es:"))

#PROCESSING
total_ganancia=(costo_toldo+costo_mesas+costo_fondo)

print("                                                      ")
#OUTPUT
print("#####################" + empresa + "  ######################")
print("cliente " + cliente )
print("fecha de emision:" + str(fecha)   )
print("################BOLETA DE VENTA#####################")
print("                                            ")
print("descripcion    " +   "   precio   " )
print("toldo            " +  str(costo_toldo))
print("fondo            " +    str(costo_fondo))
print("mesas            " +     str(costo_mesas))
print("monto total:  s/   " + str(total_ganancia))
