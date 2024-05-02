#! python3
# Usage: python3 exmp_2-1_dropped.py <initial_position> <time_interval>,
# where <initial_position> is the initial position of the ball, that is, the
# tower height in meter and time_interval is the time interval in seconds after
# the ball was dropped. If no arguments are given in command line, then the program
# will asks for the user to input those values.

"""
Example 2.1: A Ball dropped from a tower - example from the book with imrpovements.

The problem is as follows. A ball is dropped from a tower of height h. It has
initial velocity zero and accelerates downwards under gravity. The challenge
is to write a program that asks the user to enter the height in meters of the
tower and a time interval t in seconds, then prints on the screen the height of
the ball above the ground at time t after it is dropped, ignoring air resistance.

The program will compute the height of the ball above the ground using the following:
s = s_0 + vt - 0.5gt^2 with a frame of reference that has s = 0 at the ground level and
points from the ground up.
"""

import sys

g = 9.7864 # Gravitational constant in m/s^2 near IAG-USP

def position(s_0, t):
    s = s_0 - (g*t**2)/2
    return s

if __name__ == "__main__":
    if len(sys.argv) != 3:
        
        while True:
            try:
                s_0 = float(input("Enter the height of the tower in meters > 0: "))
                t = float(input("Enter the time interval > 0: "))
                if s_0 < 0 or t < 0:
                    raise ValueError("Both numbers must be greater than zero")
                break
            except ValueError as ve:
                print(ve)

    else:
        s_0 = float(sys.argv[1])
        t = float(sys.argv[2])
        if s_0 < 0 or t < 0:
            raise ValueError("Both numbers must be greater than zero")
            sys.exit(1)

    pos = position(s_0, t)

    if pos < 0:
        pos = 0
        print("In the given interval, the ball had hit the ground.")
        print("Its position is: %s m ", pos)
    else:
        print("In the given interval, the ball is at position: %.3f m" % pos)