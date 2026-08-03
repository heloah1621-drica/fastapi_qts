def calcular_descontos(valor: float, cliente_vip:bool) -> str:
    if valor < 0 or valor == 0:
        return 0.0
    if cliente_vip:
        return valor * 0.20
    else:
        return valor * 0.10
    