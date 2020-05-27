class Product:

    def __init__(self, store_type=None, name=None, price=0, *args, **kwargs):
        try:
            self.store_type = store_type
            self.name = name
            self.price = float(price)
        except Exception as e:
            print('Error in init', e)

    def __str__(self):
        return f'name {self.name} price {self.price:.2f}'

    def __repr__(self):
        return f'name {self.name} price {self.price:.2f}'

    def creat_product(self):  # куда краще записувати створений продукт щоб він не перезаписався
        print('Enter the product type')
        self.store_type = input('> ').strip()
        print('Enter the product name')
        self.name = input('> ').strip()
        print('Enter the product price')
        self.price = input('> ').strip()
        while not type(self.price) != float:
            print('Enter the product price')
            self.price = input('> ').strip()



class StorageProduct():
    profit = dict(gross_profit=0, net_profit=0)  # побачив таке на youtube (здалось так наглядніше)
    net_profit = 0
    gross_profit = 0
    storage = []

    def __str__(self):
        return f'name {Product.self.storage} price {self.price:.2f}'

    def __repr__(self):
        return f'name {Product.self.storage} price {self.price:.2f}'


    def add(self, product_obj, amount):  # додає об'єкти у список або додає кількість дло існуючого
        try:
            list_ = self.find(product_obj.name)
            list_type = self.find(product_obj.store_type)
            if list_ is None or list_type is None:
                if int(amount) or float(amount):
                    list_product = {}
                    list_product['Type'] = product_obj.store_type
                    list_product['Name'] = product_obj.name
                    list_product['Price'] = product_obj.price * 1.3
                    list_product['amount'] = float(amount)
                    self.storage.append(list_product)
            else:
                for item in self.storage:
                    if list_ == item:
                        item['amount'] += float(amount)
        except Exception as e :
            print('Error in add.there may be a lack of products', e)

    def find(self, find_product):  # повертає шуканий елемент або None
        for find_ in self.storage:
            if find_product in find_.values():
                print('YES')
                return find_
       # raise ValueError

    def sell_product(self, product_sell, amount):  # віднімає кількість проданого товару і рахує прибуток
        try:
            list_ = self.find(product_sell)
            for item in self.storage:
                if list_ == item and list_['amount'] >= float(amount):
                    item['amount'] -= float(amount)
                    profit_gross = float(amount) * item['Price']
                    profit_net = float(amount) * (item['Price'] - item['Price'] / 1.3)
                    self.profit['gross_profit'] += profit_gross
                    self.profit['net_profit'] += profit_net
                    self.gross_profit += profit_gross
                    self.net_profit += profit_net
                    return f'{product_sell} sold such quantity {amount} for the total amount {profit_gross}'
                elif list_['amount'] < float(amount):
                    raise ValueError
            return f'{product_sell} missing from the list'
        except Exception as e:
            print('Error in sell product', e)

    def get_net_profit(self):  # виводить чистий прибуток
        return f'Net profit is {self.net_profit} $'

    def get_item(self):
        return self.storage

    def get_gross_profit(self):  # виводить валовий прибуток
        return f"Gross profit is {self.gross_profit} $"

    def discount(self, product_discount, size_percent):  # робить знижку або націнку
        try:
            if float(size_percent) >= -100:
                try:
                    list_ = self.find(product_discount)
                    if list_ is not None:
                        for item in self.storage:
                            if list_ == item:
                                product_discount = []
                                product_discount.append(item)
                                item['Price'] = item['Price'] * (1 + (float(size_percent)/100))
                        return f'{product_discount} the following items have been processed'
                    return f'{product_discount} missing from the list'
                except Exception as e:
                    print('Error in discount', e)
            return f'{size_percent} too high a percentage'
        except Exception as e:
            print('Error entered not only a number', e)


# функція перевірки операції на валідність
def choice_valide(operation):
    oper_user = None
    for t in operation:
        if t in operation_valid:
            oper_user = t
            break
    return oper_user


operation_valid = {
    '1': 'create a product',
    '-': 'sell product',
    '+': 'add the product for storage',
    '?': 'check the availability of the product',
    '!': 'make a discount or markup',
    '0': 'view net income',
    '/': 'view gross profit',
    '#': 'view list Store',
    '*': 'Вихід'
}
operationToprint = [' : '.join(pretty) for pretty in operation_valid.items()]
print(*operationToprint, sep='\n')

d = Product('ford', 'super', 5)
t = Product('audi', '777', 15)
my_Store = StorageProduct()
my_Store.add(d, 6)
my_Store.add(t, '10')


try:
    while True:
        print('select the operation in the store: ')
        oper = (input('> ')).strip()
        oper = {''.join(oper)}
        oper = (choice_valide(oper))
        if oper == '*':
            print('Goodbye')
            break
        if oper == '!':
            print('Enter a discount or markup as a percentage (- / +).')
            percent_size = input('> ').strip()
            while not type(float(percent_size)) == float:
                print('You entered not only numbers. Please try again.')
                percent_size = input('> ')
            print('enter the product type or name.')
            discount_product = input('> ').strip()
            print(my_Store.discount(discount_product, percent_size))
        elif oper == '1':
            creats = Product.creat_product(Product)
        elif oper == '0':
            print(my_Store.get_net_profit())
        elif oper == '-':
            print('enter the name of the product for sale.')
            sell_product = input('> ').strip()
            print('enter sales volume.')
            sell_volume = input('> ').strip()
            while not type(sell_volume) != float:
                print('You entered not only numbers. Please try again.')
                sell_volume = input('> ').strip()
            my_Store.sell_product(sell_product, sell_volume)
        elif oper == '+':
            creats_add = Product.creat_product(Product)
            print('enter sales volume.')
            sell_volume = input('> ').strip()
            while not type(sell_volume) != float:
                print('You entered not only numbers. Please try again.')
                sell_volume = input('> ').strip()
            my_Store.add(creats_add, sell_volume)
        elif oper == '?':
            print('enter a name to verify')
            find_product = input('> ').strip()
            verify = my_Store.find(find_product)
            if verify is None:
                print(f'{find_product} not found')
            else:
                print(verify)
        elif oper == '#':
            print(my_Store.get_item())
        elif oper == '/':
            print(my_Store.get_gross_profit())
except Exception as h:
    print('Halepa', h)
