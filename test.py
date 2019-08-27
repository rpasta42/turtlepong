import turtle as t
import math
import time

import game_globals as GLOBALS
import helpers
import physics
import drawing
import keyboard_input


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


def main():

   key_bindings = keyboard_input.init_keyboard(GAME_STATE)
   drawing.init(key_bindings)

   num_frames = 0
   last_time = time.perf_counter()
   fps = 0

   while True:
      run()

      # FPS stuff
      new_time = time.perf_counter()
      if new_time - last_time >= 1:
         last_time = new_time
         fps = num_frames
         num_frames = 0
      if True:
         drawing.print_fps(fps)
      num_frames += 1

      drawing.main_loop_update()

main()

