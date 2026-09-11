#Faça um algortmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario_atual = float(input('Qual o salário do funcionário? R$'))
aumento = salario_atual * 1.15
print(f'Seu salário no valor de R${salario_atual} reais, terá um reajuste de 15%, com um aumento você ganhará R${aumento:.2f} reais.')
