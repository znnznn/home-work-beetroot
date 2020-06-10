class Animal:
    def __init__(self, sentence='sentence'):
        self.sentence = sentence

    def __str__(self):
        return f'{self.sentence}'

    def __repr__(self):
        return f'{self.sentence}'

    def talk(self):
        return self.sentence


class Dog(Animal):
    def talk(self):
        self.sentence = 'Woof'
        return self.sentence


class Cat(Animal):
    def talk(self):
        self.sentence = 'meow'
        return self.sentence


dogs = Dog()
cats = Cat()
print(dogs.talk(), cats.talk())
