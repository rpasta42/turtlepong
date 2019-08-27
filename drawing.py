import turtle as t
import time

import game_globals as GLOBALS

def init(key_bindings):
   t.speed('fastest')
   t.delay(0)
   t.hideturtle()
   t.tracer(False)
   for key, event_listener in key_bindings.items():
      t.onkey(event_listener, key)
   t.listen()

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

def print_fps(num_frames):
   #t.reset()
   #t.hideturtle()
   t.pencolor("white")
   t.setpos(-250, -250)
   t.pencolor('black')
   t.write(f'FPS {num_frames}', font=("Arial", 20, "normal"))

def main_loop_update():
   t.update()
   time.sleep(0.01)
   t.clear()



