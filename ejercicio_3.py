"""
Caso. Cree las funciones necesarias para tolerancia de una medición. Debe reutilizar una función de
valor absoluto que recibe un real y devuelve su distancia al cero. Los extremos de tolerancia se aceptan.
La función de aceptación utiliza el retorno de valor absoluto. El escenario consulta dos mediciones por
separado. Contratos en orden de parámetros: Valor absoluto: recibe real finito y devuelve real no
negativo. Aceptación: recibe medición y objetivo reales, tolerancia real no negativa y devuelve lógico.
Fórmula o relación: Error = valor absoluto de (medición − objetivo); aceptable cuando error ≤
tolerancia.
"""
def valor_abs(medida,objetivo):
    valor=medida-objetivo
    if valor<0:
        valor=valor*-1
    return valor
    
while True:
    medida_1=float(input("ingrese  primera medida:"))
    medida_2=float(input("ingrese segunda medida:"))
    objetivo=float(input("ingrese  objetivo: "))
    tolerancia=float(input("ingrese tolerancia: "))
    if tolerancia<0:
        print("\nvalores ingresados erroneos solo pueden ser positivos")
    else:
        error_1=valor_abs(medida_1,objetivo)
        error_2=valor_abs(medida_2,objetivo)
        if error_1<=tolerancia:
            resultado="verdadero"
        else:
            resultado="falso"
        if error_2<=tolerancia:
            resultado2="verdadero"
        else:
            resultado2="falso"
        print("\n aceptables: ",resultado,";",resultado2)
        break
        