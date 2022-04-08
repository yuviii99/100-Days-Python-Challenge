from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()
        if self.l_score == 5:
            self.goto(0, 0)
            self.write("Left Player Wins!", align="center", font=("Courier", 24, "normal"))

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        if self.l_score == 5:
            self.goto(0, 0)
            self.write("Left Player Wins!", align="center", font=("Courier", 24, "normal"))
            return True
        elif self.r_score == 5:
            self.goto(0, 0)
            self.write("Right Player Wins!", align="center", font=("Courier", 24, "normal"))
            return True
