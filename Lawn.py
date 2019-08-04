class Lawn(object):

    def __init__(self, upper_right_x=None, upper_right_y=None, mowers=[]):
        self.upper_right_x = upper_right_x
        self.upper_right_y = upper_right_y
        self.mowers = mowers

    def __str__(self):
        return "The lawnmowers locations are now " + str(self.mowers)
