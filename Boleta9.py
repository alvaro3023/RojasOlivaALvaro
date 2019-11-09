print("BOLETA N°9")
#INPUT
empresa=input("Nombre de la empresa: ")
fecha=input("la fecha es: ")
telefono=int(input("El numero telefonico es: "))
cajero=input("El nombre del cajero es: ")
cliente=input("El nombre del cliente es:")
costo_peluche=float(input("costo del peluche es: "))
costo_chocolate=float(input("costo de los chocolates es: "))

#PROCESSING
total_ganancia=(costo_peluche+costo_chocolate)

print("                                                      ")
#OUTPUT
print("#####################" + empresa + "  ######################")
print("                calle maria izaga 234")
print("cliente " + cliente   + "         cajero " + cajero)
print("fecha de emision:" + str(fecha)   )
print("################BOLETA DE VENTA#####################")
print("                                            ")
print("descripcion    " +   "   precio   " )
print("peluche           " +  str(costo_peluche))
print("chocolates         " +    str(costo_chocolate))
print("monto total:    s/   " + str(total_ganancia))

