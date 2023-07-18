print("Bem vindo ao quiz")
print("Deseja jogar?")
print("1. Sim")
resp = int(input("2.Não"))


if(resp == 1):
    totalPontos = 0
    
    print("Vamos começar!!")
    print("Quem descobriu o Brasil?")
    print("A. Maria")
    print("B. José")
    print("C. Felipe")
    resp1 = input("Resposta: ")
    
    if(resp1 == "A"):
        print("Resposta correta!!")
        totalPontos = totalPontos + 10
    else:
        print("Resposta incorreta") 
        
    print("Quem descobriu a frança?")
    print("A. Maria")
    print("B. José")
    print("C. Felipe")
    resp1 = input("Resposta: ")
    
    if(resp1 == "B"):
        print("Resposta correta!!")
        totalPontos = totalPontos + 10
    else:
        print("Resposta incorreta") 
        
    print("Quem descobriu o Brasil?")
    print("A. Maria")
    print("B. José")
    print("C. Felipe")
    resp1 = input("Resposta: ")
    
    if(resp1 == "C"):
        print("Resposta correta!!")
        totalPontos = totalPontos + 10
    else:
        print("Resposta incorreta") 
        
    print("Pontos totais: 30")
    print("Seus pontos: ", totalPontos)
        
elif (resp == 2):
    quit()
    
