import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def x(self):
        return self.x

    def y(self):
        return self.y

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def get_magn(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def limit(self, lim):
        while self.get_magn() > lim:
            self.x /= 2
            self.y /= 2
