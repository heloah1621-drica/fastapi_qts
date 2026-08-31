from app.descontos.descontos import calcular_descontos

def test_desconto_valor_invalido():
    resultado = calcular_descontos(-1, cliente_vip= True)
    assert round(resultado, 3) == 0

# def test_cliente_vip_com_valor_valido():
#     resultado = calcular_descontos(200.0, cliente_vip= True)
#     assert round(resultado, 3) == 20.0

# def test_cliente_nao_vip_com_valor_valido():
#     resultado = calcular_descontos(200.0, cliente_vip= False)
#     assert round(resultado, 3) == 10.0

def test_valor_positivo_muito_pequeno():
    assert round(calcular_descontos(200.0, cliente_vip=True), 3) == 40.0
    assert round(calcular_descontos(200.0, cliente_vip=False), 3) == 20.0