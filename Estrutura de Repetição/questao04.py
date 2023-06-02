# Faça um programa que receba um número e que calcule e mostre a tabuada desse número.

n = int(input("Digite um número para ver sua tabuada: "))

print(f"Tabuada do {n}:")

for a in range(1, 11):
    print(f"{n} x {a} = {n * a}")