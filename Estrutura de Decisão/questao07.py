# Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após,
# calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também
# testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',
# senão escrever a mensagem 'Saldo Negativo'.

conta = float(input("Informe a conta desejada: "))
saldo = float(input("Informe o saldo atual: "))
debito = float(input("Informe o débito: "))
credito = float(input("Informe o crédito: "))

saldo_atual = saldo - debito + credito
print(f"O saldo atual é {saldo_atual}")

if saldo_atual >= 0:
    print("Saldo POSITIVO!")
else:
    print("Saldo NEGATIVO!")