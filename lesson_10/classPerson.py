class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def talk_person(self):
        return f'Привіт, мене звати {self.name} {self.last_name} і мені  {self.age} років.'


one_person = Person('Bohdan', 'Vlasiuk', '39')
print(one_person.talk_person())
one_person.name = 'Богдан'
one_person.last_name = 'Власюк'
one_person.age = '19'
print(one_person.talk_person())
