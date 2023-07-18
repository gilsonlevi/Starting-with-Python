import random

while True:
    numeroTeto = int(input("Digite o número teto do limite"))
    random_number = random.randint(0, numeroTeto)
    
    while True:
        numero = input("Digite um número: ")
        
        if numero.isdigit():
            numero = int(numero)
        else:
            print("Por favor informe um número")
            continue
    
        if  numero == random_number:
            print("Acertou")
            break