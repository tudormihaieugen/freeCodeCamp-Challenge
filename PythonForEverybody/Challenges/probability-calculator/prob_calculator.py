import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        # get key, value for kwargs
        for key, value in kwargs.items():
            for i in range(value):
                # append keys, value times
                self.contents.append(key)

    def draw(self, number):
        # create a copy to work with
        contents_copy = self.contents
        #  if there are too many draws, get them all
        if number > len(contents_copy):
            number = len(contents_copy)
        removed_balls = []
        for i in range(number):
            # get a random position to remove ball
            position = random.randint(0, len(contents_copy) - 1)
            # create a list of removed balls
            removed_balls.append(contents_copy.pop(position))
        return removed_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # create a list with expected_balls content 
    expected_balls_contents = []
    for ball, num in expected_balls.items():
        for i in range(num):
            expected_balls_contents.append(ball)
      
    M = 0
    for x in range(num_experiments):
        # create a deep copy of hat for experiments
        hatCopy = copy.deepcopy(hat)
        # draw the given number of balls from hat copy
        drawn = hatCopy.draw(num_balls_drawn)
        flag = True
        
        # the flag will be set to False only if the contents from expected balls is not included in the random draw
        for ball in expected_balls_contents:
            if ball in drawn:
                drawn.remove(ball)
            else:
                flag = False
        # if the flag was not modified, it means that the experiment was successful
        if flag:
            M += 1

    # calculate the probabilty
    P = M / num_experiments
    return P
