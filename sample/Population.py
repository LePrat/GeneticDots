from .Dot import *
from .Brain import *
from .Obstacle import *
from .Vector import *


class Population:
    def __init__(self, size, canvas, canvas_coords, target_coords, pos, radius, color):
        self.size = size
        self.dots = []
        self.canvas_coords = canvas_coords
        self.fitness_sum = 0
        self.gen = 1
        self.best_dot = 0
        self.min_step = 400
        self.obstacles = [Obstacle(canvas, Vector(0, 2 * canvas_coords.y / 3), Vector(canvas_coords.x - 100, 10)),
                          Obstacle(canvas, Vector(200, canvas_coords.y / 3), Vector(canvas_coords.x - 100, 10))]
        for i in range(0, size):
            self.dots.append(Dot(canvas, canvas_coords, target_coords, Vector(pos.x, pos.y), radius, color, self.obstacles))

    def get_gen(self):
        return self.gen

    def show(self):
        for dot in self.dots:
            dot.show()

    def update(self):
        for dot in self.dots:
            if dot.get_brain().get_step() > self.min_step:
                dot.kill()
            else:
                dot.update()

    def calculate_fitness(self):
        for dot in self.dots:
            dot.calculate_fitness()

    def all_dead(self):
        for dot in self.dots:
            if dot.is_dead() is False and dot.has_reach_target() is False:
                return False
        return True

    def natural_selection(self):  # modify so reset dot instead of create new ones
        new_dots = []
        self.set_best_dot()
        self.calculate_sum_fitness()
        new_dots.append(self.dots[self.best_dot].pop_baby())
        new_dots[0].set_is_best()
        self.dots[0].erase()
        for i in range(1, len(self.dots)):
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
        for i in range(1, len(self.dots)):
            self.dots[i].get_brain().mutate()

    def set_best_dot(self):
        maximum = 0
        max_index = 0
        for i in range(0, len(self.dots)):
            if self.dots[i].get_fitness() > maximum:
                maximum = self.dots[i].get_fitness()
                max_index = i
        self.best_dot = max_index
        if self.dots[self.best_dot].has_reach_target():
            self.min_step = self.dots[self.best_dot].get_brain().get_step()
        print("Score:", maximum)

