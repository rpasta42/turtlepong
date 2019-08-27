import math
import sys
import helpers
import game_globals as GLOBALS

def paddle_detector(goal1_y, y):

   print(f'====goal1 {goal1_y} ball {y}')

   if goal1_y - y >= 25:
      print('tilt2')
      return 180+30
   if goal1_y - y >= 10:
      print('tilt1')
      return 180-30
   print('no tilt')
   return 180


def detect_walls(x, y, angle):

   if y > 300 or y < -300:
      print('hitting wall', x, y, angle)

   if y < -300 and 270 >= angle >= 180:
      # buttom left quad
      new_angle = angle - 180
      print('new_angle1:', new_angle)
      new_angle = 180 - 90 - new_angle
      print('new_angle2:', new_angle)
      print('old angle:', angle)
      angle -= new_angle

   return angle

i = 0
def perform_logic(GAME_STATE):
   '''
   x/y = x and y of the ball
   angle = ball direction
   goal1_y/goal2_y = goal position
   '''
   x = GAME_STATE['x']
   y = GAME_STATE['y']
   goal1_y = GAME_STATE['goal1_y']
   goal2_y = GAME_STATE['goal2_y']
   angle = GAME_STATE['ball_angle']

   global i
   i+= 1
   x = round(x, 2)
   y = round(y, 2)
   angle = round(angle, 2)

   if i % 40 == 0:
      print(f'x:{x} y:{y} goal1_y:{goal1_y} goal2_y:{goal2_y} angle:{angle}')

   if x + GLOBALS.BALL_LENGTH > GLOBALS.RIGHT_GOAL_X:
      on_paddle1 = goal1_y + GLOBALS.BALL_LENGTH >= y
      on_paddle2 = goal1_y - GLOBALS.GOAL_LENGTH <= y # 15 = half ball size; 50 = paddle size
      on_paddle = on_paddle1 and on_paddle2
      if not on_paddle:
         print('Right Lost!')
         sys.exit(-1)
      print('switching dir1', on_paddle1, on_paddle2, x,y,goal1_y, goal2_y, angle)
      #x -= 2
      angle = 180
      angle = paddle_detector(goal1_y, y)
   elif x - GLOBALS.GOAL_WIDTH <= GLOBALS.LEFT_GOAL_X:  # left ball edge touching ball
      on_paddle1 = goal2_y + GLOBALS.BALL_LENGTH >= y
      on_paddle2 = goal2_y - GLOBALS.GOAL_LENGTH <= y # 15 = half ball size; 50 = paddle size
      on_paddle = on_paddle1 and on_paddle2
      if not on_paddle:
         print('Left Lost!')
         sys.exit(-1)
      print('switching dir2', x,y,goal1_y, goal2_y, angle)
      angle = 0

   angle = detect_walls(x, y, angle)
   #h = 1 always

   rise = math.sin(helpers.torad(angle))  # o/h
   run = math.cos(helpers.torad(angle)) # a/h

   y += rise*2
   x += run*2

   GAME_STATE['x'] = x
   GAME_STATE['y'] = y
   GAME_STATE['goal1_y'] = goal1_y
   GAME_STATE['goal2_y'] = goal2_y
   GAME_STATE['ball_angle'] = angle

   return GAME_STATE


