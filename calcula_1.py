def calcular_emissoes_co2(distancia_km, num_caminhoes, consumo_km_por_litro=4, emissao_por_litro=2.68):
    """
    Calcula a emissão total de CO2 para um número específico de caminhões percorrendo uma distância específica.

    :param distancia_km: Distância percorrida em quilômetros (km)
    :param num_caminhoes: Número de caminhões
    :param consumo_km_por_litro: Consumo médio de combustível em km/litro
    :param emissao_por_litro: Emissão de CO2 por litro de diesel queimado (em kg)
    :return: Emissão total de CO2 em kg
    """
    # Calcula o consumo total de combustível em litros
    consumo_total = (distancia_km / consumo_km_por_litro) * num_caminhoes
    
    # Calcula a emissão total de CO2
    emissoes_co2_total = consumo_total * emissao_por_litro
    
    return emissoes_co2_total

def calcular_reducao_emissoes(distancia_km, num_caminhoes, consumo_km_por_litro, emissao_por_litro):
    # Emissões atuais
    emissoes_atual = calcular_emissoes_co2(distancia_km, num_caminhoes, consumo_km_por_litro, emissao_por_litro)
    
    # Emissões após a mudança (por exemplo, se o consumo melhorar)
    novo_consumo_km_por_litro = consumo_km_por_litro * 1.1  # 10% de melhoria no consumo
    emissoes_nova = calcular_emissoes_co2(distancia_km, num_caminhoes, novo_consumo_km_por_litro, emissao_por_litro)
    
    # Redução de emissões
    reducao_emissoes = emissoes_atual - emissoes_nova
    
    return reducao_emissoes, emissoes_atual, emissoes_nova

def main():
    distancia_km = float(input("Digite a distância percorrida em km por caminhão: "))
    num_caminhoes = int(input("Digite o número de caminhões: "))
    consumo_km_por_litro = float(input("Digite o consumo médio em km/litro: "))
    
    reducao_emissoes, emissoes_atual, emissoes_nova = calcular_reducao_emissoes(
        distancia_km, num_caminhoes, consumo_km_por_litro, 2.68)
    
    print(f"Emissões atuais de CO2: {emissoes_atual:.2f} kg")
    print(f"Emissões de CO2 após a mudança: {emissoes_nova:.2f} kg")
    print(f"Redução de emissões de CO2: {reducao_emissoes:.2f} kg")

if __name__ == "__main__":
    main()
