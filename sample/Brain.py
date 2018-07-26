from .Vector import *
import random
import math
import copy


class Brain:
    def __init__(self, size):
        self.size = size
        self.step = 0
        self.directions = []
        self.randomize()

    def randomize(self):
        for i in range(0, self.size):
            random_angle = random.uniform(0, 2 * math.pi)
            self.directions.append(Vector(math.cos(random_angle), math.sin(random_angle)))

    def get_direction(self):
        return self.directions

    def get_step(self):
        return self.step

    def clone(self):
        clone = Brain(len(self.directions))
        clone.get_direction().clear()
        for i in range(0, len(self.directions)):
            clone.get_direction().append(copy.deepcopy(self.directions[i]))
        return clone

    def mutate(self):
        mutation_rate = 0.01
        for i in range(0, len(self.directions)):
            rand = random.uniform(0, 1)
            if rand < mutation_rate:
                random_angle = random.uniform(0, 2 * math.pi)
                self.directions[i] = Vector(math.cos(random_angle), math.sin(random_angle))
