from .Vector import *


class Obstacle:
    def __init__(self, canvas, canvas_coord):
        self.canvas = canvas
        self.canvas_coord = canvas_coord
        self.pos = Vector(50, canvas_coord.y / 2)
        self.size = Vector(canvas_coord.x - self.pos.x * 2, 10)
        self.entity = canvas.create_rectangle(self.pos.x, self.pos.y, self.pos.x + self.size.x, self.pos.y + self.size.y, fill="red")

    def get_pos(self):
        return self.pos

    def get_size(self):
        return self.size
