import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key,value in kwargs.items():
      for i in range(value):
        self.contents.append(key)
    print(self.contents)

  def draw(self, number):
    all_removed = []
    if(number > len(self.contents)):
      return self.contents
    for i in range(number):
      removed = self.contents.pop(int(random.random() * len(self.contents)))
      all_removed.append(removed) 
    return all_removed          


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    expected_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    colors_gotten = hat_copy.draw(num_balls_drawn)

   
