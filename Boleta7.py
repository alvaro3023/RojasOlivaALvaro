print("BOLETA N°7")
#INPUT
panaderia=input("Nombre de la panaderia es: ")
cajero=input("El nombre del cajero es: ")
n_cliente=int(input("El numero de cliente es:"))
pan=float(input("Cantidad de pan pedido: "))
tarro_leche=float(input("El numero de tarros de leche es: "))
costo_tarro_leche=float(input("El costo del tarro de leche por unidad es: "))


#PROCESSING
costo_total_leche=(tarro_leche*costo_tarro_leche)
costo_total_venta=(costo_total_leche+ pan)
print("                                                      ")
#OUTPUT
print("################# BOLETA DE VENTA ##################")
print("##############" + "PANADERIA " + panaderia + "###################")
print("####################################################")
print("N° cliente :" + str(n_cliente) +  "                        cajero:" + cajero)
print("####################################################")
print("pedido   " +     "     cantidad   " +     "   prec.unit  "     +   "        total")
print("pan             "  + str(pan) +  "             .....          " +      " 1  ")
print("tarro de leche    "  + str(tarro_leche)   + "          "  + str(costo_tarro_leche) + "             " + str(costo_total_leche))
print("monto total:....................................." + str(costo_total_venta))
