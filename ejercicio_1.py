"""
Caso. Cree una función para área de un triángulo por base y altura. La altura es perpendicular a la base.
Use dos llamadas y muestre las dos áreas y su suma, calculada con los retornos. Contrato: Área de un
triángulo por base y altura: recibe base y altura, reales positivos expresados en centímetros y devuelve
el área real en centímetros cuadrados.
Fórmula o relación: Área = base × altura / 2. La división entre 2 obtiene la mitad del rectángulo de
igual base y altura.
Ejemplo de entrada Ejemplo de salida
"""
def area(base,altura):
    area=base*altura/2
    return area
while True:
    base_1=int(input("ingrese la primera base:"))
    altura_1=int(input("ingrese la primera altura:"))
    base_2=int(input("ingrese la segunda base: "))
    altura_2=int(input("ingrese la segunda altura: "))
    if base_1<0 or altura_1<0 or base_2<0 or altura_2<0:
        print("\nvalores ingresados erroneos solo pueden ser positivos")
    else:
        area1=area(base_1,altura_1)
        area2=area(base_2,altura_2)
        print("areas: ",area1," y ",area2,"cm2","\nsuma: ",area1+area2)
        break