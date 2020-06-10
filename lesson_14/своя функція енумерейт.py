def with_index(iterable, start=0):
    if start > len(iterable):
        raise ValueError
    index_list = iter(range(start, len(iterable) + start))
    for item in iterable:
        yield next(index_list), item


def in_range(start, end, step=1):
    if start > end:
        raise ValueError
    numder = start
    while numder <= end:
        yield numder
        numder += step


class My_iterable:

    def __init__(self, *args):
        self.my_iterable = args
        self.index = 0

    def __str__(self):
        return f'{self.my_iterable}'

    def __repr__(self):
        return f'{self.my_iterable}'

    def __getitem__(self, item):
        return f'{self.my_iterable[item]}'

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.my_iterable):
            raise StopIteration
        item_iterable = list(self.my_iterable[self.index])
        self.index += 1
        return item_iterable, self.index - 1


proba = 'Mamba'
newProba = ['go', 1, 2, 'terra']
newProba1 = ['lats', 3, 4, 'mars']
proba1 = My_iterable(newProba, newProba1)
result = list(with_index(proba))
print(result)
result_range = list(in_range(0, 15, 5))
print(result_range)
print(proba1)
print(proba1[1], 'hhh')
#print(next(proba1))
for item, i in proba1:
    print(item)
    print(i)
