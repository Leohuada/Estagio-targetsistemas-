import json

# Carregando os dados do arquivo JSON
with open(r'C:\Users\Pichau\Downloads\dados.json', 'r') as file:
    faturamento_diario = json.load(file)

# Filtrando dias com faturamento maior que zero
faturamento_filtrado = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]

# Calculando o menor e o maior valor de faturamento
menor_valor = min(faturamento_filtrado)
maior_valor = max(faturamento_filtrado)

# Calculando a média mensal
media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

# Calculando o número de dias com faturamento superior à média mensal
dias_acima_da_media = len([valor for valor in faturamento_filtrado if valor > media_mensal])

# Exibindo os resultados
print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Número de dias com faturamento superior à média mensal: {dias_acima_da_media}")
