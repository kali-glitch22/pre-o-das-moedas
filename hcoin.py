#!/bin/python3
import requests, json, re
red   = "\033[1;31m"
reset = "\033[0;0m"
green = "\033[0;32m"
print('-'*60)
print(red, """\n                   _..._       .-'''-.                    
                .-'_..._''.   '   _    \                  
   .          .' .'      '.\/   /` '.   \ .--.   _..._    
 .'|         / .'          .   |     \  ' |__| .'     '.  
<  |        . '            |   '      |  '.--..   .-.   . 
 | |        | |            \    \     / / |  ||  '   '  | 
 | | .'''-. | |             `.   ` ..' /  |  ||  |   |  | 
 | |/.'''. \. '                '-...-'`   |  ||  |   |  | 
 |  /    | | \ '.          .              |  ||  |   |  | 
 | |     | |  '. `._____.-'/              |__||  |   |  | 
 | |     | |    `-.______ /                   |  |   |  | 
 | '.    | '.            `                    |  |   |  | 
 '---'   '---'                                '--'   '--' \n""", reset)

requsicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
if requsicao.status_code != 200:
    print('Erro de conexão'.capitalize())
    exit()
cotacao = json.loads(requsicao.text)

preco_dolarh = cotacao['USDBRL']['high']
preco_dolarl = cotacao['USDBRL']['low']
preco_euroh = cotacao['EURBRL']['high']
preco_eurol = cotacao['EURBRL']['low']
preco_bitcoinh = cotacao['BTCBRL']['high']
preco_bitcoinl = cotacao['BTCBRL']['low']

precofdolar = re.search(r'\w+\.+\w\w',preco_dolarh).group()
precofeuro = re.search(r'\w+\.+\w\w',preco_euroh).group()
precofbitcoin = re.search(r'\w+\.+\w\w',preco_bitcoinh).group() + 'x'
precofdolarl = re.search(r'\w+\.+\w\w',preco_dolarl).group()
precofeurol = re.search(r'\w+\.+\w\w',preco_eurol).group()
precofbitcoinl = re.search(r'\w+\.+\w\w',preco_bitcoinl).group() + 'x'
print(green, f'preço alto do dólar: R${precofdolar}\n preço do alto euro: R${precofeuro}\n preço alto do bitcoin: R${precofbitcoin}'.title(), red, f'\n\n\n preço baixo do dólar: R${precofdolarl}\n preço do baixo euro: R${precofeurol}\n preço baixo do bitcoin: R${precofbitcoinl}'.title(), reset)
print('-' * 60)
