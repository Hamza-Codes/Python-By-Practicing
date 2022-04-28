import turtle # great for getting started with games. Let's us do some basic graphics. pygame is advanced.
import os

wn = turtle.Screen() # creates the screen
wn.title("Pong by @HamzaCodes")
wn.bgcolor("black") # background color of screen
wn.setup(width=800,height=600)
wn.tracer(0) # stops the window from updating so we have to update it manually


# scores

score_a = 0
score_b = 0

# Part - 2 Game Objects

# adding the paddles and ball to the screen

# Paddle A and PAddle B and the ball

# Paddle A

paddle_a = turtle.Turtle() # turtle is the name of the module/library while Turtule is the class name.

paddle_a.speed(0) # the speed of animation. Not the speed of movement of the paddle on the screen. this sets the speed of
# animation to the maximum otherwise things will be really slow.

paddle_a.shape("square") # gives the paddle a shape
paddle_a.color("white") # gives the paddle a color
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddle B

paddle_b = turtle.Turtle() # turtle is the name of the module/library while Turtule is the class name.

paddle_b.speed(0) # the speed of animation. Not the speed of movement of the paddle on the screen. this sets the speed of
# animation to the maximum otherwise things will be really slow.

paddle_b.shape("square") # gives the paddle a shape
paddle_b.color("white") # gives the paddle a color
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


# Ball

ball = turtle.Turtle() # turtle is the name of the module/library while Turtule is the class name.

ball.speed(0) # the speed of animation. Not the speed of movement of the paddle on the screen. this sets the speed of
# animation to the maximum otherwise things will be really slow.

ball.shape("square") # gives the paddle a shape
ball.color("white") # gives the paddle a color
ball.penup()
ball.goto(0,0)

# moving the ball
ball.dx = 2 #everytime the ball moves, it moves by 2 px in the x direction
ball.dy = -2 # starts the ball with negative dy



# add scording mechanism
# draw the score on the screen using the turtle library
# create a Pen using the turtle module. the turtle module give these pens a lot of different abilities.

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center",font=("Courier",24, "normal"))


# Functions - moving the paddles using the keyboard

# to move the paddle a up, we need to know the current y coordinate.
def paddle_a_up():
    y = paddle_a.ycor() # from the turtle library/module. it returns the y coordinate.
    y+=20 # adds 20 points to y coordinate when the paddle a moves up
    paddle_a.sety(y) # set the position of the paddle a to the new y coordinate

# to move the paddle a down, we need to know the current y coordinate.
def paddle_a_down():
    y = paddle_a.ycor() # from the turtle library/module. it returns the y coordinate.
    y-=20 # subtract 20 points to y coordinate when the paddle a moves up
    paddle_a.sety(y) # set the position of the paddle a to the new y coordinate


# to move the paddle a up, we need to know the current y coordinate.
def paddle_b_up():
    y = paddle_b.ycor() # from the turtle library/module. it returns the y coordinate.
    y+=20 # adds 20 points to y coordinate when the paddle a moves up
    paddle_b.sety(y) # set the position of the paddle a to the new y coordinate

# to move the paddle a down, we need to know the current y coordinate.
def paddle_b_down():
    y = paddle_b.ycor() # from the turtle library/module. it returns the y coordinate.
    y-=20 # subtract 20 points to y coordinate when the paddle a moves up
    paddle_b.sety(y) # set the position of the paddle a to the new y coordinate



# function doesn't do anything untill it is called.

# keyboard listening

wn.listen() # listen for keyboard input
wn.onkeypress(paddle_a_up,"w") # when the user presses "w", call the function paddle_a_up defined above
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up") # when the user presses "w", call the function paddle_a_up defined above
wn.onkeypress(paddle_b_down,"Down")

# Main game loop

while True: #everytime the loop runs, the screen is updated
    wn.update()

    # Move the ball continously in the x and y direction, it basically moves diagnolly. x coordinate 
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # border checking - what do we what to happen when the ball hits the borders
    # compare the ball's y coordinate and if the coordiante is over 300 om the top or 300 on the bottom then bounce it back - 
    # since the window's height is 600 px. Also the ball's height and width are 20px. 

# up and down borders

    if ball.ycor() > 290:
        ball.sety(290) # set the ball back to y = 290
        ball.dy *= -1 # reverses the direction 

    
    if ball.ycor() < -290:
        ball.sety(-290) # set the ball back to y = -290
        ball.dy *= -1 # reverses the direction

# left and right border

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center",font=("Courier",24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center",font=("Courier",24, "normal"))


# get the ball to collide with the paddles - when it touches the paddles, the direction should reverse.
# compare the x and y coordinates of the paddles and the ball

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1


# add scording mechanism
# draw the score on the screen using the turtle library
# create a Pen using the turtle module. the turtle module give these pens a lot of different abilities.

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center",font=("Courier",24, "normal"))
