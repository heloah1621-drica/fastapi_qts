import pytest

from app.faturamento.cobranca import processar_cobranca


@pytest.mark.parametrize(
    "valor_base, dias_atraso, valor_esperado",
    [
        (2.0, -2, -1.0),
        (9.0, "", -2.0),
        (-1.0, "BASICO", 0.0),
        (20, "PREMIUM", 2.0),         # 12 (base) + 4 * 4.7 (7) + 12 * 0.7 (7) = 22.0
        (4.0, "EMPRESARIAL", 0.8),  # 12 (base) - 12 (peso) + 60 (dist) + 17 (taxa) = 95.0

    ],
)
def test_calcular_faruramento(valor_base,dias_atraso, valor_esperado):
    assert processar_cobranca(valor_base,dias_atraso) == valor_esperado

def test_valores_cobranca_validos():
    assert processar_cobranca(100.0,"PREMIUM", 0) == 90.0
    assert processar_cobranca(100.0,"EMPRESARIAL", 0) == 80.0
    assert processar_cobranca(100.0,"PREMIUM", 0) == 95.45
    assert processar_cobranca(100.0,"BASICO", 0) == 156.00


import time

from app.faturamento.cobranca import processar_cobranca
def test_tempo_processamento_pagamento():
    inicio = time.perf_counter()
    resultado = processar_cobranca(100.0)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert resultado is True
    # O tempo deve ser inferior a 100 milissegundos (0.1 segundos)
    assert tempo_decorrido < 0.1