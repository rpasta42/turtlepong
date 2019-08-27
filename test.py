import turtle as t
import sys
import math
import time

import game_globals as GLOBALS
import helpers
import physics
import drawing


GAME_STATE = {
   'x': 0,
   'y': 0,
   'goal1_y': 0,
   'goal2_y': 0,
   'ball_angle': 0
}

def run():
   physics.perform_logic(GAME_STATE)

   drawing.drawball(GAME_STATE['x'], GAME_STATE['y'], GLOBALS.BALL_LENGTH)

   drawing.draw_goal(GAME_STATE['goal1_y'], False)
   drawing.draw_goal(GAME_STATE['goal2_y'], True)

def on_key_down():
   GAME_STATE['goal1_y'] -= GLOBALS.GOAL_MOVEMENT_PER_FRAME
def on_key_up():
   GAME_STATE['goal1_y'] += GLOBALS.GOAL_MOVEMENT_PER_FRAME
def on_key_w():
   GAME_STATE['goal2_y'] += GLOBALS.GOAL_MOVEMENT_PER_FRAME
def on_key_s():
   GAME_STATE['goal2_y'] -= GLOBALS.GOAL_MOVEMENT_PER_FRAME

t.onkey(on_key_up, 'Up')
t.onkey(on_key_down, 'Down')
t.onkey(on_key_w, 'w')
t.onkey(on_key_s, 's')

drawing.init()
t.listen()

def print_fps(num_frames):
   #t.reset()
   #t.hideturtle()
   t.pencolor("white")
   t.setpos(-250, -250)
   t.pencolor('black')
   t.write(f'FPS {num_frames}', font=("Arial", 20, "normal"))

import time
num_frames = 0
last_time = time.perf_counter()
fps = 0
while True:

   #t.reset()
   t.hideturtle()
   run()


   # FPS stuff
   new_time = time.perf_counter()
   if new_time - last_time >= 1:
      last_time = new_time
      fps = num_frames
      num_frames = 0
   if True or num_frames % 10 in [0, 1, 2, 3, 4, 5]:
      print_fps(fps)
   num_frames += 1

   t.update()
   time.sleep(0.01)
   t.clear()
   #t.mainloop()


