class CustomException(BaseException):
    def __init__(self, my_error):
        self.my_error = my_error

    def __str__(self):
        return f'{self.my_error}'

    def __repr__(self):
        return f'{self.my_error}'


words = open('logs.txt', 'r+')
word = words.read()
print(word)
print(len(word))
words.seek(0)
try:
    if len(word) > 0:
        for i in word:
            if ord(i) > 127:
                raise CustomException('The file contains characters that are not included in the ASCII table')
    if len(word) == 0:
        raise CustomException('this file is empty')
    elif not words.tell() == 0:
        raise CustomException('this file is not rewritten')
    elif len(word) > 3:
        raise CustomException('The file is too long, it is better to open another')
except CustomException as e:
    print(CustomException(e))


