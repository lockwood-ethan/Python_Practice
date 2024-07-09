import turtle as t
from turtle_player import TurtlePlayer
import scoreboard
import cars
import time
import random

move_speed = 0.3

screen = t.Screen()
screen.setup(width=800, height=500)
screen.colormode(255)
screen.title("Turtle Crossing")
screen.tracer(0)

level = scoreboard.Scoreboard()
player_turtle = TurtlePlayer((0, -230))

screen.listen()
screen.onkeypress(player_turtle.go_up, "w")
screen.onkeypress(player_turtle.go_down, "s")
screen.onkeypress(player_turtle.go_left, "a")
screen.onkeypress(player_turtle.go_right, "d")

game_on = True
cars_list = []
while game_on == True:
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    random_y = random.randint(-200, 240)
    random_car = cars.Car((400, random_y))
    random_car.color(R, G, B)
    cars_list.append(random_car)
    for car in cars_list:
        car.go_left()
        if car.xcor() < -400:
            cars_list.remove(car)
            car.ht()
        if player_turtle.ycor() >= 240:
            player_turtle.reset_turtle()
            level.update_score()
            move_speed *= 0.7
        if player_turtle.distance(car) <= 15:
            game_on = False      
    time.sleep(move_speed)
    screen.update()

screen.exitonclick()

