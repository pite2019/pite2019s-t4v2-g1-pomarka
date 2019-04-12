import random

class Plane:

    def __init__(self):
        self.angle = random.randint(-90, 90)
        self.orientation = random.randint(0, 1000)

    def tilt_correction(self):
        while self.angle != 0:
            if self.angle < 0:
                self.angle += 1
            else:
                self.angle -=1

    def print_angle(self):
        while TRUE:
            print(self.angle)