# Entrada de dados
idade = int(input("Digite a idade do cliente: "))
renda = float(input("Digite a renda mensal do cliente (R$): "))

# Regras de classificação
if renda >= 10000 and idade >= 30:
    categoria = "Diamante"
elif renda >= 5000:
    categoria = "Ouro"
elif renda >= 2500:
    categoria = "Prata"
else:
    categoria = "Bronze"

print(f"O cliente se enquadra na categoria: {categoria}")