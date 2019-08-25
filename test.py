import turtle as t
import time

t.speed('fastest')

def drawball(x, y, distance=20):
   t.tracer(15, 0)
   t.forward(x)
   t.right(90)
   t.forward(y)
   t.clear()

   t.tracer(7, 0)
   for i in range(0, 3):
      t.forward(distance)
      t.right(90)
   t.forward(distance)

x = 0
y = 0
def run():
   global x
   global y
   x += 1
   y += 1
   drawball(x, y)


while True:
   t.reset()
   t.hideturtle()
   run()
   time.sleep(0.1)
   t.clear()

