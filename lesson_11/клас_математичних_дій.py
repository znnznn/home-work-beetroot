class Mathematician:

    def square_nums(self, a):
        return list(map(lambda x: x ** 2, a))

    def remove_positiv(self, a):
        return list(filter(lambda x: x < 0, a))

    def even_numbers(self, a):
        r = []
        for y in a:
            if y % 2 == 0:
                r.append(y)
        return r

    def year_Leap(self, a):
        r = []
        for x, y in enumerate(a):
            if y % 4 == 0 and not y % 100 == 0:
                r.append(y)
            elif y % 400 == 0:
                r.append(y)
        return r

    def elem_sum(self, a):
        return sum(a)

    def elem_multiplace(self, a):
        f = 1
        for y in a:
            f *= y
        return f

    def average_value(self, a):
        f = 0
        for y in a:
            f += y
        average = f / len(a)
        return average


f = [1, 2, 3, 4, 5]
even = [1, 4, 16, 25, 33, 144, 254786698]
x = [7, 11, 5, 4]
positive_not = [26, -11, -8, 13, -90]
year = [2001, 1884, 1995, 2003, 2020]
t = Mathematician()
print(t.square_nums(x))
print(t.remove_positiv(positive_not))
print(t.year_Leap(year))
print(t.elem_sum(x))
print(t.elem_multiplace(f))
print(t.even_numbers(even))
print(t.average_value(f))
