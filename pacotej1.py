# _*_ coding: cp1252 _*_
import random
import math
from time import sleep
import sys


def Cts(esc):  # "Cts" quer dizer: Chutes de numeros aleatorios!, "esc" quer dizer: escolha para nos escolher um numero!
    aaa = 3  # Suas chances
    bbb = 0  # Game over
    a = math.ceil(esc * random.random())

    if aaa >= bbb:
        while aaa >= bbb:
            if aaa == bbb:
                print(f'acabou suas chances :( \n_____O numero que eu tinha escolhido era {a}_____')
                sleep(4)
                sys.exit()

            else:
                print(f'\n\nVocê tem {aaa} chances!')
                pgt = int(input(f'\nQual o numero que eu escolhi? '))

                if pgt > a:
                    print(f'Errado! O numero que eu escolhi e menor que o numero {pgt}')
                    aaa -= 1
                    sleep(2)

                elif pgt < a:
                    print(f'errado! O numero que eu escolhi e maior que o numero {pgt}')
                    aaa -= 1
                    sleep(2)

                elif pgt == a:
                    print(f'parabéns você acertou! E o numero {a}!')
                    sleep(4)
                    aaa = -1

                else:
                    print('digite um numero!')
                    sleep(1)

