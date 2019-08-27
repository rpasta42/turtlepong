import turtle as t

import game_globals as GLOBALS

def init():
   t.speed('fastest')
   t.delay(0)
   t.hideturtle()
   t.tracer(False)

def drawball(x, y, length):
   t.pencolor("white")
   t.setpos(x, y)
   t.color("black")

   #t.tracer(7, 0)
   for i in range(0, 3):
      t.forward(length)
      t.right(90)
   t.forward(length)

# starts at -300; dims: 10x50
def draw_goal(y_start, is_left):

   t.seth(0)  # set heading (reset direction turtle is facing)
   x = GLOBALS.LEFT_GOAL_X if is_left else GLOBALS.RIGHT_GOAL_X
   y = y_start
   #t.pencolor("white")
   t.penup()
   t.setpos(x, y)
   t.pendown()
   #t.color("black")

   #t.tracer(7, 0)
   t.forward(GLOBALS.GOAL_WIDTH)
   t.right(90)
   t.forward(GLOBALS.GOAL_LENGTH)
   t.right(90)
   t.forward(GLOBALS.GOAL_WIDTH)
   t.right(90)
   t.forward(GLOBALS.GOAL_LENGTH)


