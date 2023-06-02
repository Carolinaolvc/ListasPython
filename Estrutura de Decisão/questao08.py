# Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em
# estoque e quantidade mínima em estoque de um produto. Calcular e escrever a
# quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2).
# Se a quantidade em estoque for maior ou igual a quantidade média, escrever a
# mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.

q_atual = int(input("Informe a quantidade ATUAL em estoque: "))
q_max = int(input("Informe a quantidade MÁXIMA do estoque: "))
q_min = int(input("Informe a quantidade MINIMA do estoque: "))
q_med = (q_max + q_min) /2 

if q_atual >= q_med:
    print("Não efetuar compra!")
else:
    print("Efetuar compra!")