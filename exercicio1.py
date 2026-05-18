def acao_semaforo(cor: str) -> str:
    acoes = {
        "vermelho": "Pare",
        "amarelo": "Atenção",
        "verde": "Siga",
    }
    return acoes.get(cor, "Cor inválida")
