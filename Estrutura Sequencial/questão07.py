#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#1. o produto do dobro do primeiro com metade do segundo .
#2. a soma do triplo do primeiro com o terceiro.
#3. o terceiro elevado ao cubo

x = int(input("Digite um número inteiro: "))
y = int(input("Digite outro número inteiro: "))
z = float(input("Digite um número real: "))

a = (2 * x) + (y / 2)
print("O produto do dobro do primeiro com metade do segundo é: ", a)

b = (3 * x) + z
print("A soma do triplo do primeiro com o terceiro é: ", b)

c = z ** 3 
print("O terceiro elevado ao cubo é: ", c)