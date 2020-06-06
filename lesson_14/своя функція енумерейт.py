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

proba = 'Mamba'

result = with_index(proba)
print(result)
result_range = in_range(0, 15, 5)
print(result_range)