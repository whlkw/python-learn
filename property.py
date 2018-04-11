

class P:

    def __init__(self,x):
        self.x = x

    @property
    def x(self):
        print('getter')
        return self.__x

    @x.setter
    def x(self, x):
        print('setter')
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

p = P(1)
p.x = 1000
print(p.x)
