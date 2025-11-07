#Crie uma função chamada lancar_dados que utilizará o módulo random para simular o lançamento de dois dados. Cada dado deve gerar um número aleatório entre 1 e 6. A função deve somar os resultados desses dois lançamentos e retornar o valor total.

from random import randint

def lancar_dados():
    dado_um = randint(1,6)
    dado_dois = randint(1,6)
    soma = dado_um + dado_dois
    print(f"Dado um: {dado_um}\nDado dois: {dado_dois}\nSoma: {soma}")

lancar_dados()    