import pytest
from exercicio1 import acao_semaforo


class TestAcaoSemaforo:
    """Testes para a função acao_semaforo"""

    def test_vermelho_retorna_pare(self):
        assert acao_semaforo("vermelho") == "Pare"

    def test_verde_retorna_siga(self):
        assert acao_semaforo("verde") == "Siga"

    def test_amarelo_retorna_atencao(self):
        assert acao_semaforo("amarelo") == "Atenção"

    def test_cor_invalida_retorna_mensagem_erro(self):
        assert acao_semaforo("azul") == "Cor inválida"

    def test_cor_invalida_branco(self):
        assert acao_semaforo("branco") == "Cor inválida"

    def test_cor_vazia(self):
        assert acao_semaforo("") == "Cor inválida"
