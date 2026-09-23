soma = 0
maior = None
menor = None

for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    
    # Acumula a soma
    soma += numero
    
    # Define o primeiro número como referência inicial para maior e menor
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

media = soma / 5

print("\n--- RESULTADOS DA ANÁLISE ---")
print(f"Soma total: {soma}")
print(f"Média: {media:.2f}")
print(f"Maior valor digitado: {maior}")
print(f"Menor valor digitado: {menor}")