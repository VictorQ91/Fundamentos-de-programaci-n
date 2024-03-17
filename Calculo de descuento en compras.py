def calcular_descuento(monto_total, porcentaje_descuento=20):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.

    Parámetros:
    - monto_total: El monto total de la compra.
    - porcentaje_descuento: El porcentaje de descuento a aplicar (por defecto 20%).

    Devuelve:
    - El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada a la funcion
monto_total_compra = 50  # Monto total de la compra
print("Monto total de la compra: $",monto_total_compra )
descuento_calculado = calcular_descuento(monto_total_compra)  # Se calcula el descuento (20% por defecto)
print("Descuento del 20%: $", descuento_calculado) # Se muestra el valor del descuento realizado al monto total
monto_total_a_pagar= monto_total_compra - descuento_calculado # Se calcula el monto total a pagar descontado el valor del descuento
print("Monto total a pagar: $", monto_total_a_pagar)





