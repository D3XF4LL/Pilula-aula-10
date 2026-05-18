def aplicar_cupom(codigo_cupom: str, valor_compra: float) -> float:
    codigo_upper = codigo_cupom.upper()
    
    if codigo_upper == "CUPOM10":
        return 0.10
    elif codigo_upper == "CUPOM25":
        if valor_compra > 100.0:
            return 0.25
        return 0.0
    elif codigo_upper == "DESCONTOVIP":
        if valor_compra > 500.0:
            return 0.35
        return 0.0
    
    return 0.0
