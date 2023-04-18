# Valores de faturamento mensal por estado
faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcular o valor total mensal
valor_total_mensal = sum(faturamento_mensal.values())

# Calcular o percentual de representação de cada estado
percentuais = {}
for estado, valor in faturamento_mensal.items():
    percentual = (valor / valor_total_mensal) * 100
    percentuais[estado] = percentual

# Exibir os resultados
print("Percentuais de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
