def with_index(iterable, start=0):
    index_list = iter(range(start, len(iterable) + start))
    print_list = []
    for item in iterable:
        my_tuple = (next(index_list), item)
        print_list.append(my_tuple)
    return print_list


def in_range(start, end, step=1):
    my_range = []
    numder = start
    while numder <= end:
        my_range.append(numder)
        numder += step
    return my_range


class My_iterable:

    def __init__(self, *args):
        self.my_iterable = args
        self.index = 0

    def __str__(self):
        return f'{self.my_iterable}'

    def __repr__(self):
        return f'{self.my_iterable}'

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
result = with_index(proba)
print(result)
result_range = in_range(0, 15, 5)
print(result_range)
print(proba1)
#print(next(proba1))
for item, i in proba1:
    print(item)
    print(i)
