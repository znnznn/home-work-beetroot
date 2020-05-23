class PersonSchool:

    def __init__(self, name=None, last_name=None, age=None, sex=None, *args, **kwargs):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def __str__(self, *args, **kwargs):  # не виводить додаткові параметри з субкласу + не викликається метод
        return f'{self.name} {self.last_name} - {self.age} років, {self.sex} {args} {kwargs}'

    def current_person(self, *args, **kwargs):  # вертає кортеж цих елементів а при друку в стр не потрапляє
        return self.name, self.last_name, self.age, self.sex, *args, *kwargs

    def find(self, find_atr, *args, **kwargs):  # пошук для субкласів не працює а саме для додаткових характеристик
        if find_atr in self.current_person():       # завжди потрапляє типу немає по додатковим атрибутам
            return self.current_person()
        elif find_atr in (args or kwargs):
            return self.current_person()
        else:
            return f'{find_atr} особи з такими даними немає.'


class StudentSchool(PersonSchool):

    def __init__(self, name, last_name, age, sex, course=None, *args, **kwargs):
        self.course = course
        super().__init__(name, last_name, age, sex, course)

    def __str__(self):
        return PersonSchool.__str__(self)

    def current(self):
        #PersonSchool.current_person(self)
        return self.current_person(), self.course

    def find_st(self, find_atr):
        return PersonSchool.find(self, find_atr)


class TeacherSchool(PersonSchool):

    def __init__(self, name, last_name, age, sex, salary=None, *args, **kwargs):
        super().__init__(name, last_name, age, sex)
        self.salary = salary

    def find_tch(self, find_atr):
        return PersonSchool.find(self, find_atr)



list_person = [()]



x = 'f'
d = 'l'
hg = StudentSchool('f', 'd', '25', 'm', 'g')
d = PersonSchool(d, ';;;', 25)
e = PersonSchool(x)
print(d.find(25))
print(hg.find_st('g'))
print(hg.current())