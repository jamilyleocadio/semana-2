SENHA_CORRETA = "1234"
tentativas = 0
max_tentativas = 3
autenticado = False

while tentativas < max_tentativas:
    senha_digitada = input("Digite sua senha: ")
    tentativas += 1
    
    if senha_digitada == SENHA_CORRETA:
        autenticado = True
        break
    else:
        tentativas_restantes = max_tentativas - tentativas
        if tentativas_restantes > 0:
            print(f"Senha incorreta! Você ainda tem {tentativas_restantes} tentativa(s).")

if autenticado:
    print("Acesso concedido! Bem-vindo ao sistema.")
else:
    print(f"Acesso bloqueado! Você errou a senha {max_tentativas} vezes.")