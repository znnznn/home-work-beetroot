# кожна цифра числа  в квадраті
def pow_all_int(number): # приймає ціле число вертає ціле число де кожна ци
    num_str = str(number)
    new_number = ''
    for item in num_str:
        new_number += str(int(item) ** 2)
    return int(new_number)

