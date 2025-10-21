from turtle import Screen
from food import Food
from scoreboard import Score
import  time
from snack import Snack


screen=Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snack Game")


snack=Snack()
food=Food()
score=Score()
screen.listen()
screen.onkey(snack.Up,"Up")
screen.onkey(snack.Down,"Down")
screen.onkey(snack.Left,"Left")
screen.onkey(snack.Right,"Right")


is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snack.move()

    if snack.head.distance(food)<15:
        food.refresh()
        snack.extend()
        score.increase_score()
    if snack.head.xcor()>280 or snack.head.xcor()<-280 or snack.head.ycor() > 280 or snack.head.ycor()<-280:
        score.reset()
        snack.reset()

    for segment in snack.turtles[1:]:
        if snack.head.distance(segment)<10:
            score.reset()
            snack.reset()


screen.exitonclick()