class ControllerTV:

    def __init__(self, list_tv, number):
        self.name = list_tv
        self.number = number


    def getTV(self):
        for i in self.name:
            print(i, end='\n')
        return f'{self.name} +++'


    def setTV(self, name):
        if name not in self.name:
            raise ValueError('Halepa')
        print(self.name.index(name))
        return True
    my_tv = property(getTV, setTV)


channels = ["BBC", "Discovery", "TV1000", "MTV", "Sci-Fi", "GALAXY TV", "CNN"]
channels_obj = ControllerTV(channels, number=1)
print(channels_obj.getTV)
x = channels_obj.setTV("MTV")
print(x)