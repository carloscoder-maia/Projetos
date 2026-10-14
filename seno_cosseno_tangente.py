import math

angulo = float(input('Digite o ângulo que deseja calcular: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O ângulo de {angulo} tem o seno de {seno:.2f}')
print(f'O ângulo de {angulo} tem o cosseno de {cosseno:.2f}')
print(f'O ângulo de {angulo} tem a tangente de {tangente:.2f}')
