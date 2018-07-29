class Obstacle:
    def __init__(self, canvas, pos, size):
        self.canvas = canvas
        self.pos = pos
        self.size = size
        self.entity = canvas.create_rectangle(self.pos.x, self.pos.y, self.pos.x + self.size.x, self.pos.y + self.size.y, fill="red")

    def get_pos(self):
        return self.pos

    def get_size(self):
        return self.size
