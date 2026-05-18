def calcular_frete(peso_kg: float) -> float:
    if peso_kg <= 0:
        return 0.0
    elif peso_kg <= 1.0:
        return 5.0
    elif peso_kg <= 5.0:
        return 10.0
    else:
        return 18.0
