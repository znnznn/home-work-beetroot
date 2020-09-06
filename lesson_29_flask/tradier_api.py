import requests
import json

#  url = 'https://sandbox.tradier.com/v1/markets/etb'   /beta/markets/fundamentals/corporate_actions

def all_stocks():

    url = 'https://sandbox.tradier.com/v1/markets/etb'
    headers = {"Accept":"application/json",
           "Authorization":"Bearer 6ieiYLJ6rJGbWJWHXOivBDFYi7kR"}

    response = requests.request("GET", url, headers=headers)
    resp = response.json()
    stocks = open('stocks_all.json', 'w')
    json.dump(resp, stocks, indent=4)


def symbol_stocks(symbol):

    #url = f"https://api.tradier.com/v1/markets/quotes?symbols=aapl"
    url = f'https://sandbox.tradier.com/v1/markets/quotes?symbols={symbol}'
    headers = {"Accept": "application/json",
               "Authorization": "Bearer 6ieiYLJ6rJGbWJWHXOivBDFYi7kR"}
    response = requests.request("GET", url, headers=headers)
    resp = response.json()
    return resp


print(symbol_stocks("AAPL"))


""" A	NYSE MKT
B	NASDAQ OMX BX
C.	Національна фондова біржа
D	FINRA ADF
Е	Незалежний від ринку (Створено Nasdaq SIP)
F	Взаємні фонди / грошові ринки (NASDAQ)
Я	Міжнародна біржа цінних паперів
J	Прямий край A
К	Direct Edge X
М	Чиказька фондова біржа
N	NYSE
P	NYSE Arca
Питання	NASDAQ OMX
S	NASDAQ Маленька кришка
Т	NASDAQ Int
U	OTCBB
V	Позабіржове інше
W	CBOE
X	NASDAQ OMX PSX
G	GLOBEX
Y	BATS Y-обмін
Z	ЛУПИЦИ
Потоки OPRA (опції)
A	Параметри NYSE Amex
B	Біржа опцій BOX
C.	Чиказька біржа опціонів (CBOE)
H	ISE Близнюки
Я	Міжнародна біржа цінних паперів (ISE)
М	Обмін опціонами MIAX
N	Параметри NYSE Arca
О	Орган, що звітує за опціонами (OPRA)
P	МІАКС ПЕРЛИНА
Питання	Ринок опціонів NASDAQ
Т	NASDAQ OMX BX
W	C2 Обмін опціями
X	NASDAQ OMX PHLX
Z	Ринок опціонів BATS

© Tradier Inc. Всі права захищені.

 """