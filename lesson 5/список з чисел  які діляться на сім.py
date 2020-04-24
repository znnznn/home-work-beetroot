i = 0
x = 2
list_work = []
list_seven = []
while i < 100:
    i += 1
    list_work.append(i)
print(list_work)
print(list_work.index(7))
print(len(list_work))
len_work = len(list_work)
while x < len_work:
    y = list_work.index(x) % 7
    if y == 0:
        list_seven.append(list_work.index(x))
    x += 1
print(list_seven)

