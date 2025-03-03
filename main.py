""""En este proyecto, una empresa de desarrollo se dispone a crear un nuevo producto que ayude a calcular a su cliente 
(empresa contratante) la forma de pago de sus órdenes de compra. 

La empresa contratante compra diferentes piezas a una fábrica de refacciones. La empresa, dependiendo del monto total
de la compra, decidirá qué hacer para pagar al fabricante. Si el monto total de la compra excede de $500 000 la empresa
tendrá la capacidad de invertir de su propio dinero un 55% del monto de la compra, pedir prestado al banco un 30% 
y el resto lo pagara solicitando un crédito al fabricante. Si el monto total de la compra no excede de $500 000 
la empresa tendrá capacidad de invertir de su propio dinero un 70% y el restante 30% lo pagara solicitando crédito 
al fabricante. El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito. 
El monto total de la compra se calcula multiplicando el número de piezas a comprar por el precio unitario de la pieza. 
Cada orden de compra que realiza el cliente siempre es de varias unidades de una sola pieza. 
El proyecto final debe mostrar número de piezas a comprar, precio unitario de cada pieza, monto total de la compra,
inversión de la empresa, préstamo al banco y crédito al fabricante sumando el 20% que cobra de interés. 
"""
#Realizo el algoritmo:  JHINET ALEJANDRA BOHORQUEZ

def calcularMonto():
    npiezas = int(input("ingrese el numero de piezas a comprar: "))
    precioUni = float(input("ingrese el valor unitario por pieza:"))
        
    montoTotal = npiezas * precioUni
    
    if montoTotal > 500000:
        inversionEmpresa = (55*montoTotal)/100
        prestamoBanco = (30*montoTotal)/100
        creditoFabrcte = (15*montoTotal)/100     
    else:
        inversionEmpresa = (70*montoTotal)/100
        prestamoBanco = 0
        creditoFabrcte = (30*montoTotal)/100
    
    interesesfab = (creditoFabrcte*20)/100
    totalCredFab = creditoFabrcte + interesesfab
    
    print("\nResumen de la compra:")
    print(f"Número de piezas a comprar: {npiezas}")
    print(f"Precio unitario de cada pieza: ${precioUni}")
    print(f"Monto total de la compra: ${montoTotal}")
    print(f"Inversión de la empresa: ${inversionEmpresa}")
    print(f"Préstamo al banco: ${prestamoBanco}")
    print(f"Crédito al fabricante (con intereses): ${totalCredFab}")
    
calcularMonto()


