"""
Cree una función para pago semanal con horas extra. Es un modelo ficticio: las primeras 40 horas
se pagan a la tarifa ordinaria; solo las horas que exceden 40 se pagan a 1,5 veces esa tarifa. Llame para
dos personas y sume los retornos, sin redondearlos antes de sumar. Contrato: Pago semanal con horas
extra: recibe horas semanales reales no negativas y tarifa real no negativa en pesos por hora y devuelve
el pago real semanal en pesos.
Fórmula o relación: Pago = horas × tarifa si horas ≤ 40; si horas > 40, pago = 40 × tarifa + (horas −
40) × tarifa × 1,5.
"""
def pago(horas,tarifa):
    if horas<=40:
        saldo=horas*tarifa
    else:
        saldo=40*tarifa+(horas-40)*tarifa*1.5
    return saldo

while True:
    horas_1=int(input("ingrese  horas persona 1:"))
    tarifa_1=int(input("ingrese tarifa persona 1:"))
    horas_2=int(input("ingrese  horas persona 2: "))
    tarifa_2=int(input("ingrese tarifa persona 2: "))
    if horas_1<0 or tarifa_1<0 or horas_2<0 or tarifa_2<0:
        print("\nvalores ingresados erroneos solo pueden ser positivos")
    else:
        salario1=pago(horas_1,tarifa_1)
        salario2=pago(horas_2,tarifa_2)
        print("\npagos: ",salario1," y ",salario2,"\ntotal: ",salario1+salario2)
        break