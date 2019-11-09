print("EJERCICIO N°2")
#este programa calculara el precio de ganancia de la venta de polos
#INPUT
precio_compra=int(input("ingrese el valor de precio de compra:"))
precio_venta=int(input("ingrese el valor de precio de venta:"))
precio_pasajes=int(input("ingrese el valor del precio de pasajes:"))

#PROCESSING
precio_ganancia=(precio_venta - (precio_compra + precio_pasajes))

#VERIFICADOR
precio_ganancia_verificado = (precio_ganancia != 100)

#OUTPUT
print("El precio de compra es: " + str(precio_compra))
print("el precio de venta es: " + str(precio_venta))
print("el precio de los pasajes es: " + str(precio_pasajes))
print("el precio de la ganancia es: " + str(precio_ganancia))
print("el precio de la ganancia hallada es: " + str(precio_ganancia_verificado))
