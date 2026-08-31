import pytest

from app.credito.credito import classificar_credito


@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, retorno_esperado",
    [
        (0, 200, True, "renda invalida"),
        (-1, -400, True, "renda invalida"),
        (2, -30, False, "score invalido"),

        (10, 1000, True, "reprovado"),
        (8, 300, False, "reprovado"),
        (10, 500, False, "aprovado padrao"),
        (30, 900, False, "aprovado premium")
    ],
)
def test_classificar_frete_caixa_preta(
    renda_mensal, score_credito, restrito, retorno_esperado
):
    assert classificar_credito(renda_mensal, score_credito, restrito) == retorno_esperado

@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito, retorno_esperado",
    [
        
    ],
)
def test_classificar_frete_caixa_preta(
    renda_mensal, score_credito, restrito, retorno_esperado
):
    assert classificar_credito(renda_mensal, score_credito, restrito) == retorno_esperado