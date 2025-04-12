from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, cords):
        super().__init__()
        self.cords = cords
        self.penup()
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(cords)

    def up(self):
        if self.ycor() <= 230:
            self.goto(y=self.ycor() + 20 , x=self.xcor())

    def down(self):
        if self.ycor() >= -230:
            self.goto(y=self.ycor() - 20 , x=self.xcor())
