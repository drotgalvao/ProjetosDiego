import json
import numpy as np

# Carregar dados do faturamento mensal a partir do arquivo JSON
with open('faturamento_mensal.json', 'r') as file:
    faturamento_mensal = json.load(file)

# Extrair os valores de faturamento diário do JSON
faturamento_diario = np.array(faturamento_mensal['faturamento_diario'])

# Filtrar dias sem faturamento (valores iguais a 0)
faturamento_diario = faturamento_diario[faturamento_diario > 0]

# Calcular menor valor de faturamento
menor_faturamento = np.min(faturamento_diario)

# Calcular maior valor de faturamento
maior_faturamento = np.max(faturamento_diario)

# Calcular média mensal de faturamento
media_mensal = np.mean(faturamento_diario)

# Filtrar dias em que o faturamento diário foi superior à média mensal
dias_acima_da_media = len(faturamento_diario[faturamento_diario > media_mensal])

# Imprimir resultados
print("Menor valor de faturamento: R$", menor_faturamento)
print("Maior valor de faturamento: R$", maior_faturamento)
print("Número de dias com faturamento acima da média: ", dias_acima_da_media)
