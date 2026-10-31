'''Ler um ângulo em graus e mostrar o valor do seno, cosseno e tangente desse ângulo.'''

import math

# Solicita ao usuário o ângulo em graus

angulo_graus = float(input("Digite o ângulo em graus: "))

# Converte o ângulo para radianos

radianos = math.radians(angulo_graus)

# Calcula o seno, cosseno e tangente

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

# Exibe os resultados

print(f"O seno do ângulo de {angulo_graus} graus é: {seno:.2f}")
print(f"O cosseno do ângulo de {angulo_graus} graus é: {cosseno:.2f}")
print(f"A tangente do ângulo de {angulo_graus} graus é: {tangente:.2f}")