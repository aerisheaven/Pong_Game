from turtle import Turtle
ALIGN = "center"
FONT = ("Terminal", 50, "normal")


class Score(Turtle):
    def __init__(self, player):
        super().__init__()
        self.color("white")
        self.penup()
        if player == 1:
            self.setpos(-70, 220)
        elif player == 2:
            self.setpos(70, 220)
        self.hideturtle()
        self.score = 0
        self.write(f"{self.score}", align=ALIGN, font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGN, font=FONT)