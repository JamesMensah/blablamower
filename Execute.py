import logging
import sys

from Exceptions import EmptyInputFileException, WrongFormatInputFileException, MowerInitException
from Lawn import Lawn
from Mower import Mower

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


# Function that will parse and execute the instructions in the input file
def parse_and_execute_inputs(file_path):
    with open(file_path) as fp:
        # We will read the file line by line
        line = fp.readline()
        try:
            # Test if the file is empty
            if len(line.strip()) == 0:
                raise EmptyInputFileException
            if len(line) < 3:
                logging.error("The input file requires at least 3 lines")
                raise WrongFormatInputFileException
            # Init a counter of the lines
            cnt = 1
            # Let's parse each lines
            while line:
                logging.debug("Line {}: {}".format(cnt, line.strip()))
                # Check that the line is not empty
                if len(line.strip()) == 0:
                    logging.error("A line cannot be empty")
                    raise WrongFormatInputFileException
                first_char = line.strip()[0]
                second_char = line.strip()[1]
                # If we're reading the first line, we will create our square lawn
                if cnt == 1:
                    if first_char.isalpha():
                        logging.error("The lawn cannot be defined with letters")
                        raise WrongFormatInputFileException
                    if first_char != second_char:
                        logging.error("The lawn is not a square")
                        raise WrongFormatInputFileException
                    my_lawn = Lawn(int(first_char), int(second_char), [])
                    logging.debug("Creating the lawn: %s", my_lawn)
                # If not first line, let's see if we're dealing with a mower or some instructions
                else:
                    # If the first char of the line is a digit AND the line number is an even number
                    # then the line represents a mower
                    if first_char.isdigit():
                        if cnt % 2 == 1:  # If the line is odd, then it's a wrong format instruction line
                            logging.error("The instruction line has to start with a letter")
                            raise WrongFormatInputFileException
                        mower_x = int(first_char)
                        mower_y = int(second_char)
                        mower_orientation = line.strip()[2]
                        # We check that the mower is not already out of bound of the lawn
                        if mower_x > my_lawn.upper_right_x or mower_y > my_lawn.upper_right_y:
                            raise MowerInitException
                        mower = Mower(mower_x, mower_y, mower_orientation)
                        logging.debug("Found a new mower: %s", mower)
                        my_lawn.mowers.append(mower)
                        logging.debug("State of the lawn: %s", my_lawn)
                    # If the first char of the line is a letter AND line number is an odd number
                    # then the line represents the instructions
                    elif first_char.isalpha():
                        if cnt % 2 == 0:  # If the line is even, then it's a wrong format mower line
                            logging.error("The mower line has to start with a digit")
                            raise WrongFormatInputFileException
                        logging.debug("Executing mower instructions")
                        for c in line.strip():
                            # If the instruction is to go forward, We check if the next move is not ouf of bound
                            if c == "F":
                                next_move_mower = mower.__copy__()
                                next_move_mower.move(c)
                                if is_out_of_bound(next_move_mower, my_lawn):
                                    # Next move out of bound so we skip it and read the next line
                                    line = fp.readline()
                                    cnt += 1
                                    continue
                                else:
                                    mower.move(c)
                            else:
                                mower.move(c)
                            logging.debug("Mower is now: %s", mower)
                            logging.debug("State of the lawn: %s", my_lawn)
                        logging.debug("Mower final position is: %s", mower)
                    # Let's raise an exception the conditions didn't match the expected format
                    else:
                        raise WrongFormatInputFileException
                # Reading next line
                line = fp.readline()
                cnt += 1
            # When we're done reading all the lines, let's return the state of the lawn
            return my_lawn
        except EmptyInputFileException as e:
            logging.error("The Input file is empty")
            raise
        except WrongFormatInputFileException as e:
            logging.error("The format of the file is wrong")
            raise
        except ValueError as e:
            logging.error("Wrong types for some values of the mower or the instructions")
            raise
        except MowerInitException as e:
            logging.error("The mower cannot start ouf of bound of the lawn")
            raise


# Function that returns True is the next move is out of bound of the lawn
def is_out_of_bound(next_move, lawn):
    if next_move.x < 0 or next_move.y < 0:
        return True
    if next_move.x > lawn.upper_right_x or next_move.y > lawn.upper_right_y:
        return True
    else:
        return False
