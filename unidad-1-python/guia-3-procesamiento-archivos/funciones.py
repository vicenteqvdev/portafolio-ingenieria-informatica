def calcular_total_ventas(ventas):
    total_ventas = 0
    for venta in ventas:
        if venta["precio"] < 0 or venta["cantidad"] < 0:
            raise ValueError("Error: la cantidad y el precio deben ser positivos.")
        
        total_venta = venta["precio"] * venta["cantidad"]
        total_ventas = total_ventas + total_venta

    return total_ventas
