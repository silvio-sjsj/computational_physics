#! python3
# Usage: python3 exrc_2-1_dropped.py <initial_position> <initial_velocityl>,
# where <initial_position> is the initial position of the ball, that is, the
# tower height in meters and initial_velocity is the initial velocity in meters per
# seconds of the ball. If no arguments are given in command line, then the program
# will asks for the user to input those values.

"""
Exercise 2.1: Another Ball Dropped from a Tower - Here we will modify the statement to 
also request a given initial velocity (which can be zero).

A ball is again dropped from a tower of height h with a given initial velocity. Write a
program that asks the user to enter the height in meters of the tower and the ball's 
initial  velocity in meters per seconds and then calculates and prints the time the ball 
takes until it hits the ground, ignoring air resistance.

The program will compute the height of the ball above the ground using the following:
s = s_0 + vt - 0.5gt^2 with a frame of reference that has s = 0 at the ground level and
points from the ground up.
"""

import sys
from math import sqrt

g = 9.7864 # Gravitational constant in m/s^2 near IAG-USP

def time_interval(s_0, v):
    t_1 = (v - sqrt(v**2 + 2*g*s_0))/g
    t_2 = (v + sqrt(v**2 + 2*g*s_0))/g
    # Filter out negative values
    t = [t for t in (t_1, t_2) if t > 0]
    return t

if __name__ == "__main__":
    if len(sys.argv) != 3:
        
        while True:
            try:
                s_0 = float(input("Enter the height of the tower in meters > 0: "))
                v = float(input("Enter the initial velocity v in meters/second: "))
                if s_0 < 0:
                    raise ValueError("The height of the tower must be greater than zero")
                break
            except ValueError as ve:
                print(ve)

    else:
        s_0 = float(sys.argv[1])
        v = float(sys.argv[2])
        if s_0 < 0:
            raise ValueError("The height of the tower must be greater than zero")
            sys.exit(1)

    t = time_interval(s_0, v)
    t = t[0]

    print("The time interval for the ball to hit the ground is: %.3f s" % t)