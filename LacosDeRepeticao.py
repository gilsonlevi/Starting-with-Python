# i = 0 

# while i <=10:
#     print(i)
#     i = i + 1

# i = 0
# while (i < 5):
#     print(i)
#     i = i + 1

# decrescente = True

# anterior = int(input("Digite um número para iniciar:"))
# valor = 1
# while decrescente == True and valor != 0:
#     valor = int(input("Digite o proximo número:"))
#     if valor > anterior:
#         decrescente = False
#     anterior = valor

meuCartao = int(input("Digite o número do cartão de credito"))
encontrei = False
cartãoLido = 1

while cartãoLido != 0 and not encontrei:
    cartãoLido = int(input("Digite o número do cartão de credito"))
    if cartãoLido == meuCartao:
        encontrei = True