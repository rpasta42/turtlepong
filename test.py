import turtle as t
import sys
import math
import time

t.speed('fastest')
t.delay(0)
t.hideturtle()
t.tracer(False)

def drawball(x, y, distance=20):
   '''
   t.tracer(15, 0)
   t.forward(x)
   t.right(90)
   t.forward(y)
   t.clear()
   '''
   t.pencolor("white")
   t.setpos(x, y)
   t.color("black")

   #t.tracer(7, 0)
   for i in range(0, 3):
      t.forward(distance)
      t.right(90)
   t.forward(distance)

# starts at -300; dims: 10x50
def draw_goal(y_start, is_left):

   t.seth(0)

   #t.reset()
   x = -300 if is_left else 300
   y = y_start
   #t.pencolor("white")
   t.penup()
   t.setpos(x, y)
   t.pendown()
   #t.color("black")

   #t.tracer(7, 0)
   t.forward(10)
   t.right(90)
   t.forward(50)
   t.right(90)
   t.forward(10)
   t.right(90)
   t.forward(50)

def torad(deg):
   return deg * (3.14/180)

def paddle_detector(goal1_y, y):

   print(f'====goal1 {goal1_y} ball {y}')

   if goal1_y - y >= 25:
      print('tilt2')
      return 180+30
   if goal1_y - y <= -10:
      print('tilt1')
      return 180-30
   print('no tilt')
   return 180

i = 0
def perform_logic(x, y, goal1_y, goal2_y, angle):
   '''
   x/y = x and y of the ball
   angle = ball direction
   goal1_y/goal2_y = goal position
   '''
   global i
   i+= 1
   x = round(x, 2)
   y = round(y, 2)
   angle = round(angle, 2)

   if i % 40 == 0:
      print(x,y,goal1_y, goal2_y, angle)
      #time.sleep(2)

   if x > 300:
      on_paddle1 = goal1_y + 15 >= y
      on_paddle2 = goal1_y - 50 <= y # 15 = half ball size; 50 = paddle size
      on_paddle = on_paddle1 and on_paddle2
      if not on_paddle:
         print('Right Lost!')
         sys.exit(-1)
      print('switching dir1', on_paddle1, on_paddle2, x,y,goal1_y, goal2_y, angle)
      #x -= 2
      angle = 180
      angle = paddle_detector(goal1_y, y)
   elif x <= -300:
      on_paddle1 = goal2_y + 15 >= y
      on_paddle2 = goal2_y - 50 <= y # 15 = half ball size; 50 = paddle size
      on_paddle = on_paddle1 and on_paddle2
      if not on_paddle:
         print('Left Lost!')
         sys.exit(-1)
      print('switching dir2', x,y,goal1_y, goal2_y, angle)
      angle = 0

   #h = 1 always

   rise = math.sin(torad(angle))  # o/h
   run = math.cos(torad(angle)) # a/h

   y += rise*2
   x += run*2

   return x, y, goal1_y, goal2_y, angle

x = 0
y = 0
goal1_y = 0
goal2_y = 0
angle = 0
def run():
   global x, y, goal1_y, goal2_y, angle

   x, y, goal1_y, goal2_y, angle = perform_logic(x, y, goal1_y, goal2_y, angle)

   drawball(x, y)

   draw_goal(goal1_y, False)
   draw_goal(goal2_y, True)

def on_key_down():
   global goal1_y
   goal1_y -= 5
def on_key_up():
   global goal1_y
   goal1_y += 5
def on_key_w():
   global goal2_y
   goal2_y += 5
def on_key_s():
   global goal2_y
   goal2_y -= 5
t.onkey(on_key_up, 'Up')
t.onkey(on_key_down, 'Down')
t.onkey(on_key_w, 'w')
t.onkey(on_key_s, 's')

t.listen()
while True:
   t.reset()
   t.hideturtle()
   run()
   t.update()
   time.sleep(0.01)
   t.clear()
   #t.mainloop()


