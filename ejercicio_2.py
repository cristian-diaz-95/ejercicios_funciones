"""
Cree una función para precio unitario comparable. Dos paquetes pueden tener tamaños distintos;
no compare solo sus precios totales. Llame para dos paquetes y use los retornos para indicar el más
económico por gramo; si coinciden indique igualdad. Contrato: Precio unitario comparable: recibe
precio total real no negativo en pesos y cantidad real positiva en gramos y devuelve el precio real de un
gramo en pesos.
Fórmula o relación: Precio por gramo = precio total / cantidad de gramos.
"""
def precio_gr(precio,peso):
    precio_por_gramo=precio/peso
    return precio_por_gramo
while True:
    precio_1=int(input("ingrese  primera precio:"))
    peso_1=int(input("ingrese el primer peso:"))
    precio_2=int(input("ingrese  segundo precio: "))
    peso_2=int(input("ingrese segundo peso: "))
    if precio_1<0 or peso_1<0 or precio_2<0 or peso_2<0:
        print("\nvalores ingresados erroneos solo pueden ser positivos")
    else:
        precio_gr1=precio_gr(precio_1,peso_1)
        precio_gr2=precio_gr(precio_2,peso_2)
        if precio_gr1<precio_gr2:
            ganador="paquete 1"
        else:
            ganador="paquete 2"
        print("\n precios por gramo: ",precio_gr1," y ",precio_gr2,"\nconviene paquete:",ganador)
        break