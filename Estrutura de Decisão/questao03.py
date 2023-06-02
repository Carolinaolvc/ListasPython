# As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se
# forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs
# compradas, calcule e escreva o custo total da compra.

macas = int(input("Informe quantas maçãs deseja: "))

if macas >= 12:
    print(f"{macas} maçãs custam R$ {macas * 1.00:.2f}.")
else:
    print(f"{macas} maçãs custam R$ {macas * 1.30:.2f}.")   