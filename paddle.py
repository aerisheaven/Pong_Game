from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.setheading(90)
        self.penup()
        if player == 1:
            self.setpos(370, 0)
        elif player == 2:
            self.setpos(-370, 0)

    def up(self):
        self.forward(25)

    def down(self):
        self.backward(25)
