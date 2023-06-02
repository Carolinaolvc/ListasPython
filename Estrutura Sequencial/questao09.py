#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
#calcule seu peso ideal, utilizando as seguintes fórmulas:
#1. Para homens: (72.7*h) - 58
#2. Para mulheres: (62.1*h) - 44.7

h = float(input("Digite sua altura: "))
m = int((72.7 * h) - 58)
w = int((62.1 * h) - 44.7)

print(f"Se você é HOMEM, seu peso ideal é: {m} quilos.")
print(f"Se você é MULHER, seu peso ideal é: {w} quilos.")