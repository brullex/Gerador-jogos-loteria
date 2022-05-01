from random import sample
from math import factorial
import locale


def menu():
    menu = '''
[1] - Mega-Sena
[2] - Lotofacil
[3] - Quina
[4] - Lotomania
[5] - Timemania
[6] - Dupla-Sena
[7] - Dia-de-Sorte
[s] - Sair
        '''
    while True:
        print(menu)
        opcao_menu = input('Escolha uma opção: ')
        if opcao_menu == '1':
            print('#'*25, 'MEGA-SENA', '#'*25)
            print('Você pode marcar na cartela entre 6 a 15 números dos 60 disponíveis.\n')
            mega_sena()
        elif opcao_menu == '2':
            print('#'*25, 'LOTOFACIL', '#'*25)
            print('Você pode marcar na cartela entre 15 a 20 números dos 25 disponíveis:\n')
            lotofacil()
        elif opcao_menu == '3':
            print('#'*25, 'QUINA', '#'*25)
            print('Você pode marcar na cartela entre 5 a 15 números dos 80 disponíveis: \n')
            quina()
        elif opcao_menu == '4':
            print('#'*25, 'LOTOMANIA', '#'*25)
            print('Marque o maximo de 50 números dos disponíveis de 0 a 99:\n')
            lotomania()
        elif opcao_menu == '5':
            print('#'*25, 'TIMEMANIA', '#'*25)
            print('Escolha um time do coração e 10 números.\n')
            timemania()
        elif opcao_menu == '6':
            print('#'*25, 'DUPLA-SENA', '#'*25)
            print('Você pode marcar na cartela entre 6 a 15 números dos 50 disponíveis.\n')
            dupla_sena()
        elif opcao_menu == '7':
            print('#'*25, 'DIA-DE-SORTE', '#'*25)
            print('Você pode marcar na cartela entre 7 a 15 números dos 31 disponíveis.\n')
            dia_de_sorte()            
        elif opcao_menu.lower() == 's':
            print('Obrigado por usar o Gerador de números da loteria esportiva...')
            break
        else:
            print('\n \033[1;31m ### DIGITE UMA OPÇÃO VÁLIDA ### \033[0;0m' )
                   
#UMA BREVE EXPLICAÇÃO SOBRE O FUNCIONAMENTO DESTA FUNÇÃO:
#Calcula o valor da aposta usando "Combinação Simples" o valor de um jogo é calculado pela quantidade de jogos possiveis dentro
#do range de numeros escolhidos, ex: uma aposta padrao da mega-sena é de 6 números por exemplo, em uma aposta de 10 numeros, faz-se o  
#calculo da combinação simples onde chega-se há possibilidade de 210 combinações de 6 números possiveis nessa cartela com 10 numeros marcados, 
#logo o valor dessa aposta é de 210 jogos, sendo então 210 * 4,50 = 945,00.
def calc_valor_aposta(aposta, aposta_padrao, valor_aposta_padrao, qtd_apostas):
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    valor_aposta = factorial(aposta) / (factorial(aposta_padrao) * factorial(aposta - aposta_padrao)) * valor_aposta_padrao
    valor_aposta *= qtd_apostas
    print(f'\nValor da aposta: {locale.currency(valor_aposta, grouping=True)}')   

def mega_sena():
    lista_jogos = []
    aposta_padrao = 6
    valor_aposta_padrao = 4.50
    try:
        qtd_apostas = int(input('Quantas apostas deseja fazer? '))
        aposta = int(input('Quantos números deseja marcar? '))
        if qtd_apostas > 0 and aposta >= aposta_padrao:
            for i in range(qtd_apostas):
                jogo = sample(range(1, 60), aposta)
                lista_jogos.append(jogo)
        calc_valor_aposta(aposta, aposta_padrao, valor_aposta_padrao, qtd_apostas)
    except:
        print('\n \033[1;31m ### DIGITE VALORES VÁLIDOS ### \033[0;0m' )    
    for i, l in enumerate(lista_jogos):
        l.sort()
        print(f"Aposta {i + 1}º: - {', '.join(map(str,l))}")
           
def lotofacil():
    lista_jogos = []
    aposta_padrao = 15
    valor_aposta_padrao = 2.50
    try:
        qtd_apostas = int(input('Quantas apostas deseja fazer? '))
        aposta = int(input('Quantos números deseja marcar? '))
        if qtd_apostas > 0 and aposta >= aposta_padrao:
            for i in range(qtd_apostas):
                jogo = sample(range(1, 25), aposta)
                lista_jogos.append(jogo)
        calc_valor_aposta(aposta, aposta_padrao, valor_aposta_padrao, qtd_apostas)
    except:
        print('\n \033[1;31m ### DIGITE VALORES VÁLIDOS ### \033[0;0m' )       
    for i, l in enumerate(lista_jogos):
        l.sort()
        print(f"Aposta {i + 1}º: - {', '.join(map(str,l))}")

def quina():
    lista_jogos = []
    aposta_padrao = 5
    valor_aposta_padrao = 2.00
    try:
        qtd_apostas = int(input('Quantas apostas deseja fazer? '))
        aposta = int(input('Quantos números deseja marcar? '))
        if qtd_apostas > 0 and aposta >= aposta_padrao:
            for i in range(qtd_apostas):
                jogo = sample(range(1, 80), aposta)
                lista_jogos.append(jogo)
        calc_valor_aposta(aposta, aposta_padrao, valor_aposta_padrao, qtd_apostas)
    except:
        print('\n \033[1;31m ### DIGITE VALORES VÁLIDOS ### \033[0;0m' )   
    for i, l in enumerate(lista_jogos):
        l.sort()
        print(f"Aposta {i + 1}º: - {', '.join(map(str,l))}")

def lotomania():
    lista_jogos = []
    aposta_padrao = 50
    valor_aposta_padrao = 2.50
    aposta = 50
    try:
        qtd_apostas = int(input('Quantas apostas deseja fazer? '))
        if qtd_apostas > 0 and aposta >= aposta_padrao:
            for i in range(qtd_apostas):
                jogo = sample(range(0, 99), aposta)
                lista_jogos.append(jogo)
        calc_valor_aposta(aposta, aposta_padrao, valor_aposta_padrao, qtd_apostas)
    except:
        print('\n \033[1;31m ### DIGITE VALORES VÁLIDOS ### \033[0;0m' )   
    for i, l in enumerate(lista_jogos):
        l.sort()
        print(f"Aposta {i + 1}º: - {', '.join(map(str,l))}")

def timemania():
    lista_jogos = []
    lista_times = []
    aposta = 10
    aposta_padrao = 10
    valor_aposta_padrao = 2.50
    try:
        qtd_apostas = int(input('Quantas apostas deseja fazer? '))
        if qtd_apostas > 0:
            for i in range(qtd_apostas):
                time = input('Time do Coração: ')
                jogo = sample(range(1, 80), aposta)
                lista_times.append(time)
                lista_jogos.append(jogo)
        calc_valor_aposta(aposta, aposta_padrao, valor_aposta_padrao, qtd_apostas)
    except:
        print('\n \033[1;31m ### DIGITE VALORES VÁLIDOS ### \033[0;0m' )   
    for i, l in enumerate(lista_jogos):
        l.sort()
        print(f"Aposta {i + 1}º - Time do coração: {lista_times[i]} - {', '.join(map(str,l))}")

def dupla_sena():
    lista_jogos = []
    aposta_padrao = 6
    valor_aposta_padrao = 2.50
    try:
        qtd_apostas = int(input('Quantas apostas deseja fazer? '))
        aposta = int(input('Quantos números deseja marcar? '))
        if qtd_apostas > 0 and aposta >= aposta_padrao:
            for i in range(qtd_apostas):
                jogo = sample(range(1, 50), aposta)
                lista_jogos.append(jogo)
        calc_valor_aposta(aposta, aposta_padrao, valor_aposta_padrao, qtd_apostas)
    except:
        print('\n \033[1;31m ### DIGITE VALORES VÁLIDOS ### \033[0;0m' )   
    for i, l in enumerate(lista_jogos):
        l.sort()
        print(f"Aposta {i + 1}º: - {', '.join(map(str,l))}")

def dia_de_sorte():
    lista_jogos = []
    lista_meses = []
    meses = ['Janeiro', 'Fevereiro,', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    aposta_padrao = 7
    valor_aposta_padrao = 2.00
    try:
        qtd_apostas = int(input('Quantas apostas deseja fazer? '))
        aposta = int(input('Quantos números deseja marcar? '))
        if qtd_apostas > 0 and aposta >= aposta_padrao:
            for i in range(qtd_apostas):
                mes = input('Mês da sorte: ')
                if mes.capitalize() in meses:
                    jogo = sample(range(1, 80), aposta)
                    lista_meses.append(mes)
                    lista_jogos.append(jogo)
                else:
                    print('\n\033[1;31mDIGITE UM MÊS VÁLIDO!\033[0;0m') 
        calc_valor_aposta(aposta, aposta_padrao, valor_aposta_padrao, qtd_apostas)
    except:
        print('\n \033[1;31m ### DIGITE VALORES VÁLIDOS ### \033[0;0m' )   
    for i, l in enumerate(lista_jogos):
        l.sort()
        print(f"Aposta {i + 1}º - Mês da sorte: {lista_meses[i].capitalize()} - {', '.join(map(str,l))}")

# def loteca():
#     No momento não implementarei a  Loteca, devido ao estilo de jogo da mesma ser variavel de acordo com jogos de futebol da tabela,
#     do Brasileirão, o que impossibilita deixar uma tabela estatica com jogos. Assim que aprender API's encontrarei uma forma.

menu()