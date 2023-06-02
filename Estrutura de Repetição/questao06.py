# Seja criativo ao desenvolver este programa.
# a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
# b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome
# personalizado.
# c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos
# convites. Imprima o nome das pessoas que não poderão comparecer.
# d. Modifique sua lista, substitua os desistentes por novos convidados.
# e. Exiba um novo convite para cada pessoa que continua presente em sua lista.

convidados = ["Jack Chan", "Vin Diesel", "Britney Spears", "Rihanna", "Snoop Dog"]
    
for convidado in convidados:
    print(f"{convidado}, você foi convidado para um jantar na minha casa, às 19h.")

nao_vai = "Rihanna"
print(f"{nao_vai} não poderá comparecer.")