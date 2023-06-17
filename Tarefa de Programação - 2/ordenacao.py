numero1 = int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:"))
numero3 = int(input("Digite o terceiro número:"))

if numero1 < numero2 and numero1 < numero3 and numero2 < numero3:
    print("crescente")
else:
    print("não está em ordem crescente")