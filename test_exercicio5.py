import pytest
from exercicio5 import aplicar_cupom


class TestAplicarCupom:
    """Testes para a função aplicar_cupom"""

    def test_cupom_10_desconto(self):
        assert aplicar_cupom("CUPOM10", 50.0) == 0.10

    def test_cupom_10_minusculo(self):
        assert aplicar_cupom("cupom10", 50.0) == 0.10

    def test_cupom_10_misto(self):
        assert aplicar_cupom("CuPom10", 100.0) == 0.10

    def test_cupom_25_desconto_valido(self):
        assert aplicar_cupom("CUPOM25", 150.0) == 0.25

    def test_cupom_25_desconto_invalido_valor_baixo(self):
        assert aplicar_cupom("CUPOM25", 50.0) == 0.0

    def test_cupom_25_limite_minimo(self):
        assert aplicar_cupom("CUPOM25", 100.01) == 0.25

    def test_cupom_25_exatamente_100(self):
        assert aplicar_cupom("CUPOM25", 100.0) == 0.0

    def test_cupom_vip_desconto_valido(self):
        assert aplicar_cupom("DESCONTOVIP", 600.0) == 0.35

    def test_cupom_vip_desconto_invalido_valor_baixo(self):
        assert aplicar_cupom("DESCONTOVIP", 400.0) == 0.0

    def test_cupom_vip_limite_minimo(self):
        assert aplicar_cupom("DESCONTOVIP", 500.01) == 0.35

    def test_cupom_vip_exatamente_500(self):
        assert aplicar_cupom("DESCONTOVIP", 500.0) == 0.0

    def test_cupom_invalido(self):
        assert aplicar_cupom("CUPOM_FALSO", 150.0) == 0.0

    def test_cupom_invalido_minusculo(self):
        assert aplicar_cupom("cupom_falso", 150.0) == 0.0

    def test_cupom_vazio(self):
        assert aplicar_cupom("", 100.0) == 0.0

    def test_cupom_10_com_valor_zero(self):
        assert aplicar_cupom("CUPOM10", 0.0) == 0.10

    def test_cupom_10_com_valor_negativo(self):
        assert aplicar_cupom("CUPOM10", -50.0) == 0.10
