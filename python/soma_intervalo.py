#Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário. O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).

#Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.

#Ao final, exiba a soma dos números pares encontrados.
from time import sleep
inicio = int(input("Digite o valor para começar a contagem: "))
fim = int(input("Digite o valor que vai acabar a contagem: "))

soma_par = 0

for numero in range(inicio,fim+1):
    sleep(0.3)
    print(numero,end = ' ',flush=True)
    if numero % 2 == 0:
        soma_par+=numero

if soma_par > 0:
    print()
    print(f"A soma de todos os valores pares no intervalo {inicio}-{fim} é: {soma_par}.")
else:
    print()
    print(f"Nenhum numero par encontrado no intervalo {inicio}-{fim} =(.")