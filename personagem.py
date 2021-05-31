from time import sleep
class Personagem:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        self.__vida = 7 # atributo privado
        
    def __str__(self): # retorna a vida atual
        return str(self.__vida)


    def caracteristicas(self):
        while  True:
            if self.cor == 'rosa':
                print('processando...')
                sleep(0.5)
                print('Criado com sucesso!')
                print('\n')
                sleep(0.5)
                print(f'Seu personagem é um gato que se chama {self.nome} e tem a cor {self.cor}')
                sleep(0.5)
                break
            elif self.cor == 'azul':
                print('processando...')
                sleep(0.5)
                print('Criado com sucesso!')
                print('\n')
                sleep(0.5)
                print(f'Seu personagem é um gato que se chama {self.nome} e tem a cor {self.cor}')
                sleep(0.5)
                break
            elif self.cor == 'verde':
                print('processando...')
                sleep(0.5)
                print('Criado com sucesso!')
                print('\n')
                sleep(0.5)
                print(f'Seu personagem é um gato que se chama {self.nome} e tem a cor {self.cor}')
                sleep(0.5)
                break
            elif self.cor == 'branco':
                print('processando...')
                sleep(0.5)
                print('Criado com sucesso!')
                print('\n')
                sleep(0.5)
                print(f'Seu personagem é um gato que se chama {self.nome} e tem a cor {self.cor}')
                sleep(0.5)
                break
            else:
                print('Cor Inválida!')
                self.cor = input('Digite novamente: ').lower()

    def descontaVida(self):
        self.__vida -= 1

    def perdeu(self, dia):
        if self.__vida == 0:
            print('Você perdeu!')
            print(f'Quantidade de dias jogados: {dia}')
            exit()

    def nomeCor(self):
        if self.cor == 'rosa':
            return(f'\033[35m{self.nome}\033[m')
        elif self.cor == 'azul':
            return(f'\033[36m{self.nome}\033[m')
        elif self.cor == 'verde':
            return(f'\033[32m{self.nome}\033[m')
        elif self.cor == 'branco':
            return (f'{self.nome}')
            