from tkinter import *
from .Population import *
from .Dot import *
from .Vector import *


class Interface(Frame):
    def __init__(self, fenetre, **kwargs):
        self.width = 500
        self.height = 500
        self.radius = 1.5
        self.size = 300
        self.dots = []
        Frame.__init__(self, fenetre, width=self.width, height=self.height, **kwargs)
        self.pack(fill=BOTH)
        self.start_button = Button(fenetre, width=50, text="Start", fg="black", command=self.run)
        self.canvas = Canvas(self, bg="white", width=self.width, height=self.height)
        self.start_button.pack()
        self.target = Dot(self.canvas, Vector(self.width, self.height), Vector(0, 0), Vector(self.width / 2, self.radius * 3), 5, "green")
        self.population = self.pop_init()

    def pop_init(self):
        return Population(self.size, self.canvas, Vector(self.width, self.height), self.target.get_pos(), Vector(self.width / 2, self.height - self.height / 5), self.radius, "blue")

    def run(self):
        self.animation()
        self.canvas.pack()
        self.start_button.destroy()

    def animation(self):
        if self.population.all_dead() is True:
            self.population.calculate_fitness()
            self.population.natural_selection()
            self.population.mutate_babies()
            print("RESET")
        else:
            self.population.update()
            self.population.show()
        return self.after(15, self.animation)


def main():
    interface = Interface(Tk())
    interface.mainloop()


if __name__ == '__main__':
    main()
