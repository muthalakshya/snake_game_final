from turtle import Turtle
ALINGMENT = "center"
FONT = ("Aero", 28, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("orange")
        self.goto(0, 250)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score = {self.score}", align=ALINGMENT, font=FONT)


    def game_is_over(self):
        self.goto(0, 0)
        self.write("Game Over. ", align=ALINGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()