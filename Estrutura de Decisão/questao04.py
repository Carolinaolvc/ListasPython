# Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples
# e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que
# nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

nota = (nota1 + nota2) / 2

if nota >= 6:
    print(f"Sua média foi: {nota}! Parabéns! Você foi aprovado!")
else:
    print(f"Sua média foi: {nota}! Que pena! Você foi reprovado!")