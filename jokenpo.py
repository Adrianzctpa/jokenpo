import random

def jogo():
    lista = ["pedra", "papel", "tesoura"]
    escolha = input(''' Pedra papel ou tesoooouura
    ''')
    escolhadaIA = random.choice(lista)
    print(f"Você escolheu {escolha}, computador escolheu {escolhadaIA}. ")
    
    if escolha == escolhadaIA:
        print(f"Empatou! Os dois escolheram {escolha}")
    elif escolha == "pedra":
        if escolhadaIA == "tesoura":
            print("pedra quebra tesoura, você venceu!")
        else: 
            print("Papel cobre pedra, mais uma vitória para a Inteligência Artificial.")
    elif escolha == "papel":
        if escolhadaIA == "pedra":
            print("Papel cobre pedra, Você venceu, mas não faz nem sentido.") 
        else:
            print("Tesoura corta papel, mais uma solução lógica e vitória inteligente.") 
    elif escolha == "tesoura":
        if escolhadaIA == "papel":
            print("Tesoura corta papel, parabéns!")
        else: 
            print("Pedra ESMAGA tesoura! Mais uma vitória esmagadora para mim.")  

    jogardenovo = input("jogar denovo? (s/n)")
    if jogardenovo == "s":
        jogo()
    else: 
        exit    

jogo()