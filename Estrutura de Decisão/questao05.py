# Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

v1 = float(input("Informe o primeiro valor: "))
v2 = float(input("Informe o segundo valor: "))

while v1 == v2:
    print("Os valores não podem ser iguais, digite novamente: ")
    v2 = float(input("Informe o segundo valor: "))
if v1 > v2:
    print(f"O maior valor é: {v1}")
else:
    print(f"O maior valor é: {v2}")