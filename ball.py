from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0,0)
        self.y = 10
        self.x = 10
        self.movespeed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)
    
    def bounce(self):
        self.y *= -1
    
    def pbounce(self):
        self.x *= -1

    
    def lose(self):
        self.home()
        self.movespeed *= 0.9
        self.pbounce()
        