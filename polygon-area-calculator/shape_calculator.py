class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def set_width(self, width):
    self.width = width
  def set_height(self, height):
    self.height = height
  def get_area(self):
    return (self.width * self.height)
  def get_perimeter(self):
    return ( 2 * self.width + 2 * self.height)
  
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** 0.5)
  
  def get_picture(self):
    pattern = ""
    if( self.height > 50 or self.width > 50 ):
      return "Too big for picture."
    for i in range(self.height):
      for j in range(self.width):
          pattern = pattern + '*'
      pattern = pattern + "\n"
    return pattern  

  def get_amount_inside(self, name):
    oth = name.get_area()
    own = self.get_area()
    c = 0
    while own >= oth:
      own = own - oth
      c = c + 1
    return c
  
  def __str__(self):
    return "Rectangle(width="+ str(self.width) + ", height=" + str(self.height) + ")"

class Square(Rectangle):
   def __init__(self, side):
     self.side = side
   
   def set_side(self, side):
     self.side = side

   def get_area(self):
    return (self.side ** 2)
   
   def set_width(self, width):
     self.side = width 

   def get_diagonal(self):
    return (self.side * (2 ** 0.5))

   def get_perimeter(self):
    return ( 2 * self.side + 2 * self.side)
   
   def get_picture(self):
    pattern = ""
    for i in range(self.side):
      for j in range(self.side):
          pattern = pattern + '*'
      pattern = pattern + "\n"
    return pattern
     
   def __str__(self):
    return "Square(side="+ str(self.side) + ")"