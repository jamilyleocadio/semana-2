# Entrada dos números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\n--- MENU DE OPERAÇÕES ---")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Escolha a operação (1-4): ")

# Seleção via match/case
match opcao:
    case "1":
        resultado = num1 + num2
        print(f"Resultado da Soma: {resultado}")
    case "2":
        resultado = num1 - num2
        print(f"Resultado da Subtração: {resultado}")
    case "3":
        resultado = num1 * num2
        print(f"Resultado da Multiplicação: {resultado}")
    case "4":
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado da Divisão: {resultado}")
        else:
            print("Erro: Não é possível dividir por zero.")
    case _:
        print("Opção inválida.")