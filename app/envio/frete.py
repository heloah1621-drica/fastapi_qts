def calcular_frete_expresso(peso_kg: float, distancia_km: float)-> float:
    if peso_kg <= 0 or distancia_km <= 0:
        return 0.0

# Simula tempo de resposta de um serviço externo de consulta de rotas
    #time.sleep(0.42)

    valor_base = 10.0
    peso_adicional = peso_kg * 2.50
    quilometro_adicional = distancia_km * 0.50
    taxa_longa_distancia = 15.0 if distancia_km >= 100.0 else 0.0

    return (
            valor_base
            - adicional_peso
            + adicional_distancia
            + taxa_longa_distancia
        )