from .Dot import *
from .Brain import *


class Population:
    def __init__(self, size, canvas, canvas_coords, target_coords, pos, radius, color):
        self.size = size
        self.dots = []
        self.canvas_coords = canvas_coords
        self.fitness_sum = 0
        self.gen = 1
        for i in range(0, size):
            self.dots.append(Dot(canvas, canvas_coords, target_coords, Vector(pos.x, pos.y), radius, color))

    def show(self):
        for dot in self.dots:
            dot.show()

    def update(self):
        for dot in self.dots:
            dot.update()

    def calculate_fitness(self):
        for dot in self.dots:
            dot.calculate_fitness()

    def all_dead(self):
        for dot in self.dots:
            if dot.is_dead() is False and dot.has_reach_target() is False:
                return False
        return True

    def natural_selection(self):
        new_dots = []
        self.calculate_sum_fitness()
        for i in range(0, len(self.dots)):
            parent = self.select_parent()
            new_dots.append(parent.pop_baby())
            self.dots[i].erase()
        self.dots = new_dots
        self.gen += 1

    def calculate_sum_fitness(self):
        self.fitness_sum = 0
        for dot in self.dots:
            self.fitness_sum += dot.get_fitness()

    def select_parent(self):
        rand = random.uniform(0, self.fitness_sum)
        running_sum = 0
        for dot in self.dots:
            running_sum += dot.get_fitness()
            if running_sum > rand:
                return dot
        return None

    def mutate_babies(self):
        for dot in self.dots:
            dot.get_brain().mutate()

    # def reset_dots(self):
    #     for dot in self.dots:
    #         dot.ressurect()
    #         dot.set_pos(Vector(self.canvas_coords.x / 2, self.canvas_coords.y - self.canvas_coords.y / 5))
    #         dot.set_brain()

