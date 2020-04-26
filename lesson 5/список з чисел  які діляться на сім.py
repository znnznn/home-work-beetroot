i = 0
list_work = []
list_seven = []
while i < 100:
    i += 1
    list_work.append(i)
print(list_work)
for list_seven in list_work:
    if list_seven % 7 == 0 and not list_seven % 5:
        print(list_seven, end=' ')
