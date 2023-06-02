# Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em
# ordem crescente.

v1 = float(input("Informe o primeiro valor: "))
v2 = float(input("Informe o segundo valor: "))

while v1 == v2:
    print("Os valores não podem ser iguais, digite novamente: ")
    v2 = float(input("Informe o segundo valor: "))
if v1 > v2:
    print(v2, v1, sep=" / ")
else:
    print(v1, v2, sep=" / ")