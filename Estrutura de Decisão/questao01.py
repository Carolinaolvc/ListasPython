# Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou
# menor que 10. O programa deve escrever a mensagem correspondente (maior ou
# menor) e informar o valor digitado pelo usuário.

v = float(input("Digite um valor numérico: "))

if v >= 10:
    print(f"{v} é um valor MAIOR que 10!")
else:
    print(f"{v} é um valor MENOR que 10!")