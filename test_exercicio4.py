import pytest
from exercicio4 import calcular_bonus


class TestCalcularBonus:
    """Testes para a função calcular_bonus"""

    def test_bonus_bom(self):
        assert calcular_bonus(1000.0, "Bom") == 100.0

    def test_bonus_excelente(self):
        assert calcular_bonus(1000.0, "Excelente") == 200.0

    def test_bonus_regular(self):
        assert calcular_bonus(1000.0, "Regular") == 20.0

    def test_bonus_ruim(self):
        assert calcular_bonus(1000.0, "Ruim") == 0.0

    def test_bonus_avaliacao_invalida(self):
        assert calcular_bonus(1000.0, "Mais ou Menos") == 0.0

    def test_bonus_salario_negativo_excelente(self):
        assert calcular_bonus(-1000.0, "Excelente") == 0.0

    def test_bonus_salario_negativo_bom(self):
        assert calcular_bonus(-500.0, "Bom") == 0.0

    def test_bonus_salario_zero_excelente(self):
        assert calcular_bonus(0.0, "Excelente") == 0.0

    def test_bonus_valores_diferentes_excelente(self):
        assert calcular_bonus(5000.0, "Excelente") == 1000.0

    def test_bonus_valores_diferentes_regular(self):
        assert calcular_bonus(5000.0, "Regular") == 100.0
