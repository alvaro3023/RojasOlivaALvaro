print("BOLETA N°5")
#INPUT
empresa=input("Nombre de la empresa es: ")
R_U_C=int(input("El numero de R.U.C es:"))
caja=int(input("El numero de caja es: "))
cajero=input("El nombre de la cajera es: ")
cliente=input("El nombre del cliente es:")
radio=int(input("Cantidad de radios comprados: "))
costo_radio=float(input("El costo de la radio por unidad es: "))
tv=int(input("La cantidad de tv comprados es : "))
costo_tv=float(input("El precio del tv por unidad es: "))

#PROCESSING
total_costo_radio=(radio* costo_radio)
total_costo_tv=(tv*costo_tv)
total_venta=(total_costo_radio+total_costo_tv)

print("                                                      ")
#OUTPUT
print("#####################" + " " + empresa +" ######################")
print("                calle Pedro Ruiz")
print("R.U.C  " + str(R_U_C))
print("cliente  " + cliente + "   caja  " + str(caja) + "  cajero  " + cajero)
print("################BOLETA DE VENTA#####################")
print("                                            ")
print("electrodomestico     " + "    cantidad    " +  "   precio   " +   "    total")
print("radio        " + "               " + str(radio)  +   "            "  +   str(costo_radio)  + "         "  +  str(total_costo_radio))
print("tv                          "  + str(tv) + "           " + str(costo_tv) + "           " + str(total_costo_tv))
print("monto total:            s/   " + str(total_venta))
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("Donde todo es más barato! ")
