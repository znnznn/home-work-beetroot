class Dog:
    age_factor = 7

    def __init__(self, age_factor=age_factor):
        self.age_factor = age_factor

    def human_age(self):
        self.human_age = self.age_factor * 7 + self.age_factor
        return f'Вік собаки  {self.age_factor} років в еквіваленті віку людини складає  {self.human_age} років.'


one_dog = Dog
print(one_dog.human_age(one_dog))
