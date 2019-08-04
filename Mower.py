import logging

from Exceptions import WrongFormatInputFileException


class Mower(object):

    def __init__(self, x=int, y=int, orientation=str):
        self.x = x
        self.y = y
        self.orientation = orientation

    def __str__(self):
        return "Mower(" + str(self.x) + ";" + str(self.y) + ";" + self.orientation + ")"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.orientation == other.orientation:
            return True
        else:
            return False

    def __copy__(self):
        return type(self)(self.x, self.y, self.orientation)

    def move(self, instruction=None):
        if instruction == "F":
            if self.orientation == "N":
                self.y = self.y + 1
            elif self.orientation == "S":
                self.y = self.y - 1
            elif self.orientation == "E":
                self.x = self.x + 1
            elif self.orientation == "W":
                self.x = self.x - 1
            else:
                logging.error("This orientation is not valid")
                raise WrongFormatInputFileException
        elif instruction == "L":
            if self.orientation == "N":
                self.orientation = "W"
            elif self.orientation == "S":
                self.orientation = "E"
            elif self.orientation == "W":
                self.orientation = "S"
            elif self.orientation == "E":
                self.orientation = "N"
            else:
                logging.error("This orientation is not valid")
                raise WrongFormatInputFileException
        elif instruction == "R":
            if self.orientation == "N":
                self.orientation = "E"
            elif self.orientation == "S":
                self.orientation = "W"
            elif self.orientation == "W":
                self.orientation = "N"
            elif self.orientation == "E":
                self.orientation = "S"
            else:
                logging.error("This orientation is not valid")
                raise WrongFormatInputFileException
        else:
            logging.error("This instruction is not valid")
            raise WrongFormatInputFileException
