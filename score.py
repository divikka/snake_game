from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"score:{self.score} highscore:{self.highscore}",move=False, align="center", font=("Arial", 16, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")
            self.update()

    # def over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align="center", font=("Arial", 26, "normal"))
    def increase(self):
        self.score += 1
        self.update()
