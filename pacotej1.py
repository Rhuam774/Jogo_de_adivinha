import random
import math
from time import sleep


def Cts(esc):  # "Cts" quer dizer: Chutes de numeros aleatorios!, "esc" quer dizer: escolha para nos escolher um numero!
    aaa = 3  # Suas chances
    bbb = 0  # Game over
    a = math.ceil(esc * random.random())

    if aaa >= bbb:
        while aaa > bbb:
            pgt = int(input('\n\nQual o numero que escolhi?'))

            if pgt > a:
                print('Errado! meu numero e menor que o numero escolhido')
                aaa -= 1
                sleep(2)

            elif pgt > a:
                print('errado! meu numero e maior que o numero escolhido')
                aaa -= 1
                sleep(2)

            elif pgt == a:
                print('parabéns você acertou!!')
                sleep(4)
                aaa = -1

    elif aaa == bbb:
        print('acabou suas chances :( ')
