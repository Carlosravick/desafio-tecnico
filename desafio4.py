# Programa para calcular o percentual de faturamento por estado

# Definição dos faturamentos por estado
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}


total_faturamento = sum(faturamento.values())

print("Percentual de representação por estado:")
for estado, valor in faturamento.items():
    percentual = (valor / total_faturamento) * 100
    print(f"{estado}: {percentual:.2f}%")
