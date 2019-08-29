

class Shape:
   pass

class Rectange(Shape):
   pass
class Square(Shape):
   pass
class Circle(Shape):
   pass
class Polygon(Shape):
   pass


class Vertex:
   def __init__(self, x, y, z=0):
      pass

class Image:
   def __init__(self, path):
      pass
   pass

class Node:

   def __init__(self):
      pass

   def get_children(self):
      # [ {'type': 'image/shape', ... } ]
      pass

   def get_parent(self):
      pass

   def set_position(self, position):
      pass

   def move(self, angle, distance):
      pass

   def translate(self, vector):
      pass

   def scale(self, factor):
      pass

   def rotate(self, angle):
      pass


   def add_image(self, image):
      pass # returns item_id

   def add_shape(self, blah):
      pass # returns item_id

   def new_node(self):
      pass

   pass



