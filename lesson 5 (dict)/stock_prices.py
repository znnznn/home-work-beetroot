stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
all_value = 0
for key_prices in prices:
    for key_stock in stock:
        if key_prices == key_stock:
            all_value += stock[key_stock] * prices[key_prices]
print(all_value)
