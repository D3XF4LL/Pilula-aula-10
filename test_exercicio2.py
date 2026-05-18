import pytest
from exercicio2 import calcular_frete


class TestCalcularFrete:
    """Testes para a função calcular_frete"""

    def test_frete_ate_1_kg(self):
        assert calcular_frete(1.0) == 5.0

    def test_frete_abaixo_1_kg(self):
        assert calcular_frete(0.5) == 5.0

    def test_frete_acima_1_ate_5_kg(self):
        assert calcular_frete(3.0) == 10.0

    def test_frete_limite_5_kg(self):
        assert calcular_frete(5.0) == 10.0

    def test_frete_pouco_acima_1_kg(self):
        assert calcular_frete(1.01) == 10.0

    def test_frete_pouco_acima_5_kg(self):
        assert calcular_frete(5.01) == 18.0

    def test_frete_peso_zero(self):
        assert calcular_frete(0) == 0.0

    def test_frete_peso_negativo(self):
        assert calcular_frete(-10) == 0.0

    def test_frete_peso_grande(self):
        assert calcular_frete(100.0) == 18.0
