import turtle as trtl

wn = trtl.Screen()

plr = trtl.Turtle()

obs = trtl.Turtle()
obs.ht()
obs.penup()
obs.setheading(180)
obs.goto(obs.xcor() + 300, obs.ycor() + 25)
obs.st()
obs.speed(0.51)

passable = False

def jump():
  plr.speed(0.51)
  plr.goto(plr.xcor(), plr.ycor() + 100)
  if obs.xcor() > plr.xcor() + 50 and obs.xcor() > plr.xcor():
    print('passable')
    move_obstacle(obs)
  else:
    print("DEADASS")

def move_obstacle(obstacle):
  wn.listen()
  wn.onkey(jump, 'space')
  obs.forward(350)
  if plr.ycor() > 0:
    print("passed")
    plr.goto(plr.xcor(), plr.ycor() - 100)

##wn.onkey(jump, 'space')

move_obstacle(obs)

wn.listen()
wn.mainloop()