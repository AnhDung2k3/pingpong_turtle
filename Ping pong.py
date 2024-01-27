from turtle import Turtle, Screen
import time

display = Screen()
display.setup(800, 600)
display.bgcolor("black")
display.title("Ping pong game")
display.tracer(0)

class scroll_bar(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(pos)
    
    def moveUp(self):
        y_pos = self.ycor() + 20
        self.goto(self.xcor(), y_pos)

    def moveDown(self):
        y_pos = self.ycor() - 20
        self.goto(self.xcor(), y_pos)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.shape("circle")
        self.penup()
        self.distance_move_x = 10
        self.distance_move_y = 10
        self.ball_speed = 0.2

    def moveBall(self):
        x_pos = self.xcor() + self.distance_move_x
        y_pos = self.ycor() + self.distance_move_y
        self.goto(x_pos, y_pos)

    def ball_touch_width(self):
        self.distance_move_y *= -1

    def ball_touch_scrollbar(self):
        self.distance_move_x *= -1
        self.ball_speed *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.distance_move_x *= -1
        self.ball_speed = 0.2

class ScorePlayer(Turtle):
    def __init__(self):
        super.__init__()
        self.color("White")
        self.penup()
        self.playerLeft = 0
        self.playerRight = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-80, 250)
        self.write(self.playerLeft, align = "center", font = ("Arial", 40, "Normal"))
        self.goto(80, 250)
        self.write(self.playerRight, align = "center", font = ("Arial", 40, "Normal"))

    def leftScore(self):
        self.playerLeft += 1
        self.update_score()
    
    def rightScore(self):
        self.playerRight += 1
        self.update_score()

scroll_bar_right = scroll_bar((350, 0))
scroll_bar_left = scroll_bar((-350, 0))

ball = Ball()

score_player = ScorePlayer()

display.listen()
display.onkey(scroll_bar_right.moveUp, "Up")
display.onkey(scroll_bar_right.moveDown, "Down")
display.onkey(scroll_bar_left.moveUp, "w")
display.onkey(scroll_bar_left.moveDown, "s")

start_game = True
while start_game:
    time.sleep(ball.ball_speed)
    display.update()
    ball.moveBall()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_touch_width()
    
    if ball.distance(scroll_bar_right) < 50 and ball.xcor() > 330:
        ball.ball_touch_scrollbar()
    
    if ball.distance(scroll_bar_left) < 50 and ball.xcor() < -330:
        ball.ball_touch_scrollbar()
    
    if ball.xcor() > scroll_bar_right.xcor() + 20:
        ball.reset_ball()
        score_player.leftScore()

    if ball.xcor() < scroll_bar_left.xcor() - 20:
        ball.reset_ball
        score_player.rightScore()

display.exitonclick()