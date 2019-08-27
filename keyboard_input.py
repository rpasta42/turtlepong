
def init_keyboard(GAME_STATE):
   def on_key_down():
      GAME_STATE['goal1_y'] -= GLOBALS.GOAL_MOVEMENT_PER_FRAME
   def on_key_up():
      GAME_STATE['goal1_y'] += GLOBALS.GOAL_MOVEMENT_PER_FRAME
   def on_key_w():
      GAME_STATE['goal2_y'] += GLOBALS.GOAL_MOVEMENT_PER_FRAME
   def on_key_s():
      GAME_STATE['goal2_y'] -= GLOBALS.GOAL_MOVEMENT_PER_FRAME

   key_bindings = {
      'Up': on_key_up,
      'Down': on_key_down,
      'w': on_key_w,
      's': on_key_s
   }
   return key_bindings


