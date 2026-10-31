'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

from random import choice

# Nome dos alunos

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Lista com os nomes dos alunos

Alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(Alunos)  # Escolhe um aluno aleatoriamente

# Escolhe um aluno aleatoriamente

print(f"O aluno escolhido foi: {escolhido}")