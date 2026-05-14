import random
import numpy as np

# EXERCÍCIO 1
# Matriz 3x3 com números aleatórios

matriz = []

for linha in range(3):
    nova_linha = []

    for coluna in range(3):
        numero = random.randint(1, 10)
        nova_linha.append(numero)

    matriz.append(nova_linha)

print("Matriz 3x3:")
for linha in matriz:
    print(linha)

# EXERCÍCIO 2
# Soma de matrizes de vendas

vendas_semana1 = [
    [10, 20],
    [15, 30]
]

vendas_semana2 = [
    [5, 10],
    [20, 25]
]

resultado = []
total_geral = 0

for i in range(2):
    linha = []

    for j in range(2):
        soma = vendas_semana1[i][j] + vendas_semana2[i][j]

        linha.append(soma)

        total_geral += soma

    resultado.append(linha)

print("\nSoma das matrizes:")
for linha in resultado:
    print(linha)

print("Total geral:", total_geral)

# EXERCÍCIO 3
# Média de alunos usando NumPy

notas = np.array([
    [7.5, 8.0, 9.0],
    [6.0, 5.5, 7.0],
    [9.5, 8.5, 10.0]
])

medias = np.mean(notas, axis=1)

print("\nNotas dos alunos:")
print(notas)

print("\nMédias:")
print(medias)

# EXERCÍCIO 4
# Determinante da matriz

matriz_sistema = np.array([
    [2, 1, 3],
    [1, 0, 2],
    [4, 1, 8]
])

determinante = np.linalg.det(matriz_sistema)

print("\nDeterminante:", determinante)

if determinante != 0:
    print("O sistema é resolvível.")
else:
    print("O sistema NÃO é resolvível.")

# EXERCÍCIO 5
# Transposta e multiplicação de matrizes

estoque = np.array([
    [10, 5],
    [20, 8]
])

precos = np.array([
    [2],
    [4]
])

transposta = estoque.T

totais = np.dot(transposta, precos)

print("\nMatriz transposta:")
print(transposta)

print("\nTotais:")
print(totais)
