import turtle
#import playsound
import winsound

# Main window
wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_a.penup()
paddle_a.goto(-350, 0)    

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_b.penup()
paddle_b.goto(350, 0) 

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0) 

ball.dx = 0.15 # delta x
ball.dy = 0.15 # delta y

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: 0 Player B: 0", align="center", font=("Arial", 20, "normal"))


#Functions
def paddle_a_up(): # move A up
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down(): # move A down
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up(): # move B up
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down(): # move B down
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def updateScore(): # update the Score
    pen.clear()
    pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Arial", 20, "normal"))

#keyboard binding
wn.listen()
#paddle A
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
#paddle B
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290: # Top border
        ball.sety(290)
        ball.dy *= -1
        print(ball.dy)
        winsound.PlaySound("sound\Wall.wav", winsound.SND_ASYNC) # play sound

    if ball.ycor() < -290: # Bottom boder
        ball.sety(-290)
        ball.dy *= -1
        print(ball.dy)
        winsound.PlaySound("sound\Wall.wav", winsound.SND_ASYNC) # play sound

    if ball.xcor() > 385: # rigth border
        ball.setx(385)
        ball.dx *= -1
        print(ball.dx)

        winsound.PlaySound("sound\Point.wav", winsound.SND_ASYNC) # play sound

        score_a += 1 # score update
        updateScore()


    if ball.xcor() < -380: # left border
        ball.setx(-380)
        ball.dx *= -1
        print(ball.dx)

        winsound.PlaySound("sound\Point.wav", winsound.SND_ASYNC) # play sound

        score_b += 1 # score update
        updateScore()


    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and ((ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor() - 40)):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("sound\Paddle.wav", winsound.SND_ASYNC) # play sound

    if (ball.xcor() < -340 and ball.xcor() > -350) and ((ball.ycor() < paddle_a.ycor() + 40) and (ball.ycor() > paddle_a.ycor() - 40)):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("sound\Paddle.wav", winsound.SND_ASYNC) # play sound