print("BOLETA N°8")
#INPUT
hotel=input("Nombre del hotel: ")
R_U_C=int(input("El numero de R.U.C es:"))
telefono=int(input("El numero telefonico es: "))
fecha=input("ingrese la fecha: ")
hora=input("ingrese la hora:")
recepcionista=input("El nombre del recepcionista es: ")
cliente=input("El nombre del cliente es:")
costo_cuarto=float(input("costo del cuarto por dia es: "))
dias_hospedado=int(input("N°de dias hospedado es: "))

#PROCESSING
total_ganancia=(costo_cuarto*dias_hospedado)

print("                                                      ")
#OUTPUT
print("#####################" + hotel + "  ######################")
print("                calle av.grau.1120")
print("R.U.C  " + str(R_U_C))
print("cliente " + cliente   + "         recepcionista " + recepcionista)
print("fecha de emision:" + str(fecha)    + "     hora:" + str(hora))
print("################BOLETA DE VENTA#####################")
print("                                            ")
print("descripcion    " + "    dias/hospedado   " +  "   precio   " +   "    total")
print("hab.305            " + "    " + str(dias_hospedado)  +   "            "  +   str(costo_cuarto)  + "           "  +  str(total_ganancia))
print("monto total:   ....................    s/   " + str(total_ganancia))
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("a su servicio siempre....")
