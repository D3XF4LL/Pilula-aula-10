def converter_nota_para_conceito(nota: float) -> str:
    if nota < 0 or nota > 10:
        return "Nota inválida"
    elif nota >= 9.0:
        return "A"
    elif nota >= 7.0:
        return "B"
    elif nota >= 5.0:
        return "C"
    elif nota >= 3.0:
        return "D"
    else:
        return "F"
