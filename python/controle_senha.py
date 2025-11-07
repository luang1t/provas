#Crie um programa em Python que simule um sistema de login. O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.

login = "admin"
senha = "coxinha123"

tentativas = 3

print("SISTEMA DE LOGIN")
while tentativas !=0:
    login_input = str(input("Digite seu login: "))
    senha_input = str(input("Digite sua senha: "))
    tentativas-=1

    if login != login_input and senha != senha_input:
        if tentativas!=0 and tentativas!=1:
            print(f"Errou, ainda restam {tentativas} tentativas.")

        elif tentativas == 1:
            print(f"Errou, sua ultima tentaiva!")

    else:
        print("Boas Vindas!")
        break
         
    if tentativas == 0:
        for _ in range(3):
            print("Conta bloqueada depois de 3 tentativas =(")
