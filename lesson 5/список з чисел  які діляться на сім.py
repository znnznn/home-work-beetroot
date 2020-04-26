ii = 0
list_work = list(range(1, 101))
list_seven = []
print(list_work)
for list_seven in list_work:
    if list_seven % 7 == 0 and not list_seven % 5:
        print(list_seven, end=' ')
