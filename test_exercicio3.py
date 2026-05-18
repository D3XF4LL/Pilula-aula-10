import pytest
from exercicio3 import converter_nota_para_conceito


class TestConverterNotaParaConceito:
    """Testes para a função converter_nota_para_conceito"""

    def test_nota_perfeita_conceito_a(self):
        assert converter_nota_para_conceito(10.0) == "A"

    def test_nota_limite_minimo_a(self):
        assert converter_nota_para_conceito(9.0) == "A"

    def test_nota_conceito_b(self):
        assert converter_nota_para_conceito(8.0) == "B"

    def test_nota_limite_maximo_b(self):
        assert converter_nota_para_conceito(8.9) == "B"

    def test_nota_limite_minimo_b(self):
        assert converter_nota_para_conceito(7.0) == "B"

    def test_nota_conceito_c(self):
        assert converter_nota_para_conceito(6.0) == "C"

    def test_nota_limite_maximo_c(self):
        assert converter_nota_para_conceito(6.9) == "C"

    def test_nota_limite_minimo_c(self):
        assert converter_nota_para_conceito(5.0) == "C"

    def test_nota_conceito_d(self):
        assert converter_nota_para_conceito(4.0) == "D"

    def test_nota_limite_maximo_d(self):
        assert converter_nota_para_conceito(4.9) == "D"

    def test_nota_limite_minimo_d(self):
        assert converter_nota_para_conceito(3.0) == "D"

    def test_nota_abaixo_3_conceito_f(self):
        assert converter_nota_para_conceito(2.9) == "F"

    def test_nota_zero_conceito_f(self):
        assert converter_nota_para_conceito(0.0) == "F"

    def test_nota_negativa_invalida(self):
        assert converter_nota_para_conceito(-1.0) == "Nota inválida"

    def test_nota_acima_10_invalida(self):
        assert converter_nota_para_conceito(11.0) == "Nota inválida"
