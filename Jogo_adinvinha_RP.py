# _*_ coding: cp1252 _*_
#wwwwwwwwwwwwwwwwwwwwwwww cadeia de importa��es wwwwwwwwwwwwwwwwwwwwwwww

import pacotej1
from os import system
from time import sleep
#wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww

pgt1 = input('Ol� digite seu nome: ')  # "pgt" quer dizer: pergunta, e os numeros s�o pra enumerar cada pergunta
print('\n')
system('cls')

print('Seja bem-vindo ', pgt1, '\n')
sleep(2)

print('Vamos come�ar? :)\n')
sleep(1)
system('cls')
print('Irei escolher um numero de acordo com a dificuldade que voc� escolher e voc� tem 3 chances para adivinhar o numero!')
pgt2 = input('\nAgora escolha uma dificuldade; digite 1 para Facil, digite 2 para Medio, digite 3 para dificil: ')


if pgt2 == '1':
    print('irei escolher um numero entre 1 e 5!\n _____pronto?_____')
    sleep(2)
    print('\n\n')
    pacotej1.Cts(5)

elif pgt2 == '2':
    print('irei escolher um numero entre 1 e 10!\n _____pronto?_____')
    sleep(2)
    print('\n\n')
    pacotej1.Cts(10)

elif pgt2 == '3':
    print('irei escolher um numero entre 1 e 15!\n _____pronto?_____')
    sleep(2)
    print('\n\n')
    pacotej1.Cts(15)

else:
    print('Voc� n�o digitou ou digitou errado e por isso o jogo foi fechado')