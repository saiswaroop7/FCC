import copy
import random, sys
from collections import Counter
# Consider using the modules imported above.

class Hat:
  def __init__(self, **args):
    self.contents = [""] * sum(args[i] for i in args)
    c = 0
    self.rands = [0] * len(self.contents)
    for i in args:
      for j in range(args[i]):
       self.contents[c] = str(i)
       c = c + 1
    self.li2 = copy.deepcopy(self.contents) 
    return None
  
  def draw(self, amount):
    self.contents = copy.deepcopy(self.li2)
    if(amount > len(self.contents)):
      return self.contents
    else:
     self.drawn = [""] * amount
     for i in range(amount):
        randint = random.randint(0, len(self.contents) -1 )
        self.drawn[i] = self.contents[randint]
        self.contents.pop(randint)
        self.rands[i] = randint
     return self.drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  t = num_experiments
  prob = 0.0
  mas = 0.0

  while(t > 0):
   drawn = hat.draw(num_balls_drawn)
   to = Counter(drawn)
   z = {}
   for i in to: z[i] = to[i]
   m = 0
   for i in expected_balls:
     try:
      if(z[i] >= expected_balls[i]):
           m = m + 1
      else:
        t = t - 1       
        break
      if(int(m)==len(expected_balls)):
        mas = mas + 1
        t = t-1
     except :
      t = t - 1
      break
   hat.contents = hat.contents + drawn
  prob = round(float(mas/num_experiments),3)
  return prob
