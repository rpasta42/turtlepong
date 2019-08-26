import turtle as t
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
   return deg/360 * (3.14/180)

i = 0
def perform_logic(x, y, goal1_y, goal2_y, angle):
   '''
   x/y = x and y of the ball
   angle = ball direction
   goal1_y/goal2_y = goal position
   '''
   global i
   i+= 1
   if i % 40 == 0:
      print(x,y,goal1_y, goal2_y, angle)
      #time.sleep(2)

   if x > 300:
      print('switching dir1', x,y,goal1_y, goal2_y, angle)
      x -= 2
      angle = 180
   elif x <= -300:
      print('switching dir2', x,y,goal1_y, goal2_y, angle)
      angle = 0

   #h = 1 always

   rise = math.sin(torad(angle))  # o/h
   run = math.cos(torad(angle)) # a/h

   if angle >= 0 and angle <= 90:
      #print('forward', angle)
      #x += 1
      #y += 1*y_over_x
      y += rise
      x += run
   elif angle >= 180:
      #print('backward', angle)
      # x -= 1
      # y -= 1

      #x -= 1
      #y += y_over_x
      x -= run
      y -= rise

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
   time.sleep(0.02)
   t.clear()
   #t.mainloop()


