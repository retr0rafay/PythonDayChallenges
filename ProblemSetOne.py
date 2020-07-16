import math


# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0
# and n.


class GeneratorClass:
    def __init__(self, number):
        self.number = number

    def classGenerator(self):
        for num in range(self.number):
            if num % 7 == 0:
                yield num


g_class = GeneratorClass(int(input("Please enter a number: ")))
generator = g_class.classGenerator()
while True:
    try:
        get_next_number = input("Would you like to get the next number? ")
        if get_next_number.lower() == 'yes':
            print(next(generator))
        else:
            break
    except StopIteration:
        print('You are done!')
        break


# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
# with a given steps. The trace of robot movement is shown as the following:
#
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
#
# The numbers after the direction are steps. Please write a program to compute the
# distance from current position after a sequence of movement and original point. If the distance is a float,
# then just print the nearest integer. Example: If the following tuples are given as input to the program:
#
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
#
# 2

# Distance formula is sqrt((x2-x1)^2 - (y2 - y1)^2)

def getDistance():
    up_travel_point = 0
    down_travel_point = 0
    left_travel_point = 0
    right_travel_point = 0
    while True:
        travel_point = input().split()
        if not travel_point:
            break
        if travel_point[0].lower() == 'up':
            up_travel_point = (travel_point[0], int(travel_point[1]))
        elif travel_point[0].lower() == 'down':
            down_travel_point = (travel_point[0], int(travel_point[1]))
        elif travel_point[0].lower() == 'left':
            left_travel_point = (travel_point[0], int(travel_point[1]))
        elif travel_point[0].lower() == 'right':
            right_travel_point = (travel_point[0], int(travel_point[1]))

    get_distance = math.sqrt(
        (up_travel_point[1] - down_travel_point[1]) ** 2 + (left_travel_point[1] - right_travel_point[1]) ** 2)
    return int(get_distance)


distance = getDistance()
print(distance)
