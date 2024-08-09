def calcular_emissoes_co2_por_caminhao():
    """
    Calcula a emissão de CO2 para um caminhão que passa por uma barreira de pedágio sem parada.

    :return: Emissão de CO2 por caminhão em kg
    """
    # Distância em km para redução e aceleração de velocidade
    distancia_km = 0.5
    
    # Consumo de combustível durante a redução e aceleração (km/l)
    consumo_km_por_litro = 4
    
    # Emissão de CO2 por litro de diesel (kg)
    emissao_por_litro = 2.68
    
    # Consumo durante a redução e aceleração de velocidade
    consumo_total = distancia_km / consumo_km_por_litro
    
    # Emissões durante a redução e aceleração de velocidade
    emissoes_totais = consumo_total * emissao_por_litro
    
    return emissoes_totais

def calcular_emissoes_totais(num_caminhoes):
    """
    Calcula a emissão total de CO2 para um número específico de caminhões.

    :param num_caminhoes: Número de caminhões
    :return: Emissão total de CO2 em kg
    """
    emissoes_por_caminhao = calcular_emissoes_co2_por_caminhao()
    emissoes_totais = emissoes_por_caminhao * num_caminhoes
    
    return emissoes_totais

def main():
    num_caminhoes = int(input("Digite o número de caminhões: "))
    emissoes_totais = calcular_emissoes_totais(num_caminhoes)
    
    print(f"Emissão total de CO2 para {num_caminhoes} caminhões: {emissoes_totais:.2f} kg")

if __name__ == "__main__":
    main()
