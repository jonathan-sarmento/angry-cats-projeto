from random import sample
from relogio import Relogio
from personagem import Personagem
from os import system
from time import sleep

clear = lambda:system('cls') # função que limpa a tela
enter = lambda:input('\nPressione ENTER para continuar...') # função que dá uma pausa no programa

def menu(): # menu de opcoes
    print('[ 1 ] Autores')
    print('[ 2 ] Objetivo do jogo')
    print('[ 3 ] Sair do jogo')
    print('[ 4 ] Voltar')
    op = int(input('>> '))

    if op == 1: 
        print('*'*70)
        print('''Autores: \033[36mJonathan Sarmento Sousa\033[m, \033[34mLuana Melissa O. Silva\033[m
                    Turma 2 C - Noite''')
        print('*'*70)
    elif op == 2: 
        print('*'*150)
        print('''
Aqui, o objetivo é não ficar parado. Você é um gato que possui 7 vidas para mostrar seu talento com travessuras! Seu objetivo é estressar 
seu dono. Serão apresentadas opções e cada uma delas tem um tempo de execução, suas travessuras não podem passar de 2 horas e tem que 
cumprir um prazo mínimo de 1 hora e meia de execução. E aí,''', str(gato.nomeCor()+','), '''você acha que dá conta?''')
        print('\n')
        print('*'*150)
    elif op == 3:
        print('****FIM DE JOGO****')
        exit()
    elif op == 4:
        pass
    else:
        print('Opção inválida')
        enter()
        clear()
        menu()

def escolha(opcoes):
    global tempo
    aux = list(opcoes.keys())
    aux = list(sample(aux, 2))
    for p, x in enumerate(aux):  
        print(f'{p+1} - {x}')
    
    print('3 - Parar e aguardar o seu dono')
    print('\n[ 0 ] Menu')
    op = int(input('>> '))
    if op == 0:
        clear()
        menu() # Menu de opcoes
    elif 1 <= op <= 2:
        tempo.Tempogasto(opcoes[aux[op-1]])
        del opcoes[aux[op-1]]
        # print(tempo)
    elif op == 3:
        if tempo.horas*60 + tempo.minutos >= 480 + 30: # Se o tempo estiver no intervalo | 480 + 30 = 8:30
            print('Parabéns, você conseguiu estressar o seu dono com sucesso!')
            enter()
            return True
        else: # Se o tempo for menor que 8:30
            print('Você não atingiu o tempo mínimo de bagunça!')
            gato.descontaVida()
            print(f'Vidas restantes: {gato}')
            gato.perdeu(dia)
            enter()
            return True
    else:
        print('Opção inválida!')
    return False


if __name__ == '__main__': # main

    # <cadastro>
    print('*'*80)
    print('{:^80}'.format('\33[33mANGRY CATS\33[m'))
    print('*'*80)
    sleep(0.8)
    print('{:^70}'.format('BEM VINDO AO ANGRY CATS'))
    sleep(0.8)
    print('{:^80}'.format('Para começarmos a nos divertir escolha o nome e a cor do seu personagem!'))
    sleep(0.8)
    print('\n')
    nome = str(input('Digite o nome do seu personagem: ')).title()
    print('\n')
    sleep(0.8)

    print(' \33[35mRosa\33[m  \33[36mAzul\33[m  \33[32mVerde\33[m  Branco')
    cor = str(input('Digite a cor de sua preferência: ')).lower()
    print('\n')
    sleep(0.8)
    gato = Personagem(nome, cor) 
    gato.caracteristicas()
    sleep(3)
    print('\n'*2)
    # </cadastro> 
    clear()
    dia = 1
    relogio = Relogio()
    # <enredo>
    print('*'*150)
    print('''
    Aqui, o objetivo é não ficar parado. Você é um gato que possui 7 vidas para mostrar seu talento com travessuras! Seu objetivo é estressar 
    seu dono. Serão apresentadas opções e cada uma delas tem um tempo de execução, suas travessuras não podem passar de 2 horas e tem que 
    cumprir um prazo mínimo de 1 hora e meia de execução. E aí,''', str(gato.nomeCor()+','), '''você acha que dá conta?''')
    print('\n')
    print('*'*150)
    enter()
    print('\n'*2)
    print('criando cenário...')
    print('\n')
    sleep(1)
    # </enredo>
    
    while True:
        clear()
        opcoes = {
        'Derrubar a tv': 20, 'Arranhar o sofá': 30, 'Urinar na cama': 15, 'Fazer cocô no teclado do notebook': 20, 'Rasgar o saco de ração': 15, 'Vomitar bolas de pelo pela casa': 30, 'Derrubar os livros da estante': 15, 'Iniciar uma reunião com os outros gatos da vizinhança':30, 'Chamar os gatos da vizinhança, fazer uma festa e deixar tudo sujo':50}
        tempo = Relogio()
        print(f'Dia {dia}')
        print('Seu dono saiu para uma caminhada matinal, são '  + str(relogio)  + ' horas e você tem até 09:00 horas para cumprir o objetivo do jogo!')
        enter()
        clear()
        print('O que você quer fazer primeiro?')
        sleep(1)

        while True:
            clear()
            print(f'{gato.nomeCor()} escolha uma das opções:')
            if escolha(opcoes):
                break 
            
            if tempo.Tempofinal():
                print('Você estrapolou o tempo e foi pego no flagra pelo seu dono!')
                gato.descontaVida()
                print(f'Vidas restantes: {gato}')
                gato.perdeu(dia)
                enter()
                break
            enter()
        dia += 1