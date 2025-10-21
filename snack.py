from symtable import Class
from turtle import  Turtle

STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVING=20

UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snack:
    def __init__(self):
        self.turtles = []
        self.create_snack()
        self.head=self.turtles[0]

    def create_snack(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
    def add_segment(self,position):
        timmy = Turtle("square")
        timmy.color("white")
        timmy.penup()
        timmy.goto(position)
        self.turtles.append(timmy)
    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def move(self):
        for segment in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[segment - 1].xcor()
            new_y = self.turtles[segment - 1].ycor()
            self.turtles[segment].goto(new_x, new_y)
        self.head.forward(MOVING)

    def reset(self):
        for turtle in self.turtles:
            turtle.goto(1000,1000)
        self.turtles.clear()
        self.create_snack()
        self.head = self.turtles[0]


    def Up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def Down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def Left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def Right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

