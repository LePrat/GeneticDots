from .Brain import *
from .Vector import *
import math
import copy


class Dot:
    def __init__(self, canvas, canvas_coords, target_coords, pos, radius, color, obstacles=None):
        self.brain = Brain(400)
        self.radius = radius
        self.pos = pos
        self.start_pos = copy.deepcopy(pos)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.canvas = canvas
        self.fix = 10
        self.color = color
        self.canvas_coords = canvas_coords
        self.target_coords = target_coords
        self.obstacles = obstacles
        self.dead = False
        self.reach_target = False
        self.is_best = False
        self.entity = [self.canvas.create_oval(pos.x, pos.y, pos.x + self.radius * 2, pos.y + self.radius * 2, fill=color, outline =""),
                       self.canvas.create_oval(pos.x - self.fix, pos.y - self.fix, pos.x + self.radius * 2 + self.fix, pos.y + self.radius * 2 + self.fix, fill="", outline="")]
        self.fitness = 0

    def show(self):
        if self.is_best is True:
            best_size = 3
            self.canvas.itemconfig(self.entity[0], fill="orange", outline="black")
            self.canvas.coords(self.entity[0], self.pos.x - best_size, self.pos.y - best_size, self.pos.x + self.radius * 2 + best_size, self.pos.y + self.radius * 2 + best_size)
            self.canvas.coords(self.entity[1], self.pos.x - self.fix, self.pos.y - self.fix, self.pos.x + self.radius * 2 + self.fix, self.pos.y + self.radius * 2 + self.fix)
            self.canvas.tag_raise(self.entity[0])
        else:
            self.canvas.coords(self.entity[0], self.pos.x, self.pos.y, self.pos.x + self.radius * 2, self.pos.y + self.radius * 2)
            self.canvas.coords(self.entity[1], self.pos.x - self.fix, self.pos.y - self.fix, self.pos.x + self.radius * 2 + self.fix, self.pos.y + self.radius * 2 + self.fix)

    def set_pos(self, pos):
        self.pos.x = pos.x
        self.pos.y = pos.y

    def get_pos(self):
        return self.pos

    def is_dead(self):
        return self.dead

    def kill(self):
        self.dead = True

    def set_is_best(self):
        self.is_best = True

    def has_reach_target(self):
        return self.reach_target

    def ressurect(self):
        self.dead = False
        self.reach_target = False

    def set_velocity(self, velocity):
        self.velocity.x = velocity.x
        self.velocity.y = velocity.y

    def get_velocity(self):
        return self.velocity

    def get_radius(self):
        return (self.canvas.coords(self.entity[0])[2] - self.canvas.coords(self.entity[0])[0])/2

    def set_brain(self):
        self.brain = Brain(400)

    def get_brain(self):
        return self.brain

    def get_fitness(self):
        return self.fitness

    def move(self):
        if len(self.brain.get_direction()) > self.brain.step:
            self.acceleration = self.brain.get_direction()[self.brain.step]
            self.brain.step += 1
        else:
            self.dead = True
        self.velocity.add(self.acceleration)
        self.velocity.limit(6)
        self.pos.add(self.velocity)

    def update(self):
        if self.dead is False and self.reach_target is False:
            self.move()
            self.touch_wall()
            self.touch_target()
            self.touch_obstacle()

    def touch_wall(self):
        if (self.pos.x + self.get_radius() * 2 >= self.canvas_coords.x or
                self.pos.x < 0 or
                self.pos.y + self.get_radius() * 2 > self.canvas_coords.y or
                self.pos.y < 0):
            self.dead = True

    def touch_target(self):
        interval = 10
        if (self.target_coords.x <= self.pos.x + self.get_radius() <= self.target_coords.x + interval and
                self.target_coords.y - interval <= self.pos.y + self.get_radius() <= self.target_coords.y + interval):
            self.reach_target = True

    def touch_obstacle(self):
        if self.obstacles is not None:
            for obstacle in self.obstacles:
                if obstacle.get_pos().x <= self.pos.x + self.get_radius() <= obstacle.get_pos().x + obstacle.get_size().x and \
                        obstacle.get_pos().y <= self.pos.y + self.get_radius() <= obstacle.get_pos().y + obstacle.get_size().y:
                    self.dead = True

    def calculate_fitness(self):
        if self.reach_target is True:
            self.fitness = 1.0/16.0 + 10000.0 / (self.brain.get_step() * self.brain.get_step())
        else:
            distance_to_goal = math.sqrt(math.pow(self.target_coords.x - self.pos.x, 2) + math.pow(self.target_coords.y - self.pos.y, 2))
            self.fitness = 1 / math.pow(distance_to_goal, 3)

    def pop_baby(self):
        baby = Dot(self.canvas, self.canvas_coords, self.target_coords, Vector(self.start_pos.x, self.start_pos.y), self.radius, self.color, self.obstacles)
        baby.brain = self.brain.clone()
        return baby

    def erase(self):
        self.canvas.delete(self.entity[0])
        self.canvas.delete(self.entity[1])
