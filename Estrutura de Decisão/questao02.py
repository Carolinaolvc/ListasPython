#  Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou
# negativo (considere o valor zero como positivo).

v = float(input("Digite um valor numérico: "))

if v >= 0:
    print(f"{v} é um valor positivo!")
else:
    print(f"{v} é um valor negativo!")