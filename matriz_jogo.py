import random #importando a biblioteca random

characters = []
def catch_characters(): 
    print('INSIRA O NOME DOS PERSONAGENS!!')
    stop = 'sim'
    while stop != 'não': 
        characters.append(input('DIGITE O NOME DO PERSONAGEM: '))#adicionando personagens ao array
        stop = (str(input('Deseja continuar: ')))#flag de parada

def figths():
    print(characters)
    champion = str(input('ESCOLHA O SEU PERSONAGEM: '))
    while champion == '?':#caso escolhido personagem aleatorio o jogo decide
        champion = random.choice(characters)
        if champion != '?':
            break
    characters.remove(champion)#remove o personagem escolhido dos disponiveis
    random.shuffle(characters)#embaralha o array de oponentes
    for i in range(len(characters)):
        print(f'LUTA ENTRE {champion} vs {characters[i]}')#decide a luta contra o oponente

catch_characters()
figths()    