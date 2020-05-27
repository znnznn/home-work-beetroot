class Product:

    def __init__(self, store_type=None, name=None, price=0, *args, **kwargs):
        self.store_type = store_type
        self.name = name
        self.price = float(price)

    def __str__(self):
        return f'name {self.name} price {self.price:.2f}'

    def __repr__(self):
        return f'name {self.name} price {self.price:.2f}'


class StorageProduct(Product):
    amount = 0
    net_profit = 0
    gross_profit = 0
    storage = []

    def __str__(self):
        return f'name {self.name} price {self.price:.2f}'

    def __repr__(self):
        return f'name {self.name} price {self.price:.2f}'

    def add(self, product_obj, amount):  # додає об'єкти у список або додає кількість дло існуючого
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

    def find(self, find_product):  # повертає шуканий елемент або None
        for find_ in self.storage:
            if find_product in find_.values():
                print('YES')
                return find_
       # raise ValueError

    def sell_product(self, product_sell, amount):  # віднімає кількість проданого товару і рахує прибуток
        list_ = self.find(product_sell)
        print(list_, 'fjfjfjf')
        for item in self.storage:
            if list_ == item and list_['amount'] >= float(amount):
                item['amount'] -= float(amount)
                self.gross_profit += float(amount) * item['Price']
                self.net_profit += float(amount) * (item['Price'] - item['Price'] / 1.3)
        print(f'{list_} missing from the list')

    def get_net_profit(self):  # виводить чистий прибуток
        return f"Net profit is {self.net_profit} $"

    def get_item(self):
        return map(lambda x: x[0], self.storage)

    def get_gross_profit(self):  # виводить валовий прибуток
        return f"Gross profit is {self.gross_profit} $"

    def discount(self, product_discount, size_percent):  # робить знижку
        list_ = self.find(product_discount.name)
        list_type = self.find(product_discount.store_type)
        count_item = 0
        for item in self.storage:
            if list_ is None or list_type is None:
                count_item += 1
                print(item)
                product_discount.price = product_discount.price * (1 - (size_percent/100))

            else:
                return f'{item} missing from the list'






d = Product('k', 'p', 5)
t = Product('j', 'p', 15)
print(type(d))
k = StorageProduct()
k.add(d, 6)
print(StorageProduct.find(k, 'k'))
k.add(t, '10')
print(StorageProduct.storage)
print(StorageProduct.find(k, 'j'))
print(k.sell_product('k', 5))
print(StorageProduct.storage, k.get_net_profit())
print(k.get_gross_profit())
print(k.discount(k, 20))
print(k.get_item())
