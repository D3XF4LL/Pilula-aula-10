def calcular_bonus(salario_base: float, avaliacao: str) -> float:
    if salario_base < 0:
        return 0.0
    
    percentuais = {
        "Excelente": 0.20,
        "Bom": 0.10,
        "Regular": 0.02,
    }
    
    percentual = percentuais.get(avaliacao, 0.0)
    return salario_base * percentual
