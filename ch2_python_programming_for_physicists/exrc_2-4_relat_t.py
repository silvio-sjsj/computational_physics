#! python3
# Usage: python3 exrc_2-4_relat_t.py <distance> <velocity>, where <distance> and
# <velocity> are the distance in light years from Earth to the planet and the velocity
# as a fraction of c of the spaceship. Given both arguments, the program calculate the
# time interval for reaching the planet in the rest frame of Earth and as perceived
# by the passenger on the spaceship.
# If no arguments are given in command line, then the program
# will asks for the user to input those values.

""""
Exercise 2.4: A spaceship travels from Earth in a straight line at relativistic speed v
to another planet x light years away. Write a program to ask the user for the value of x
and the speed v as a fraction of the speed of light c, then print out the time in years
that the spaceship takes to reach its destination
(a) in the rest frame of an observer on Earth, and
(b) as perceived by a passenger on board the ship.
Use your program to calculate the answers for a planet 10 light years away with v=0.99c.
"""

import sys
from math import sqrt

def compute_t(x, v):
    """Computes the proper time and the relativistic time for given inputs x and v"""

    lorentz_factor = 1/sqrt(1 - v**2)
    t_relativistic = x/v
    t_proper = t_relativistic/lorentz_factor

    return t_relativistic, t_proper

if __name__ == "__main__":
    if len(sys.argv) != 3:
        
        while True:
            try:
                x = float(input("Enter the distance x in light years: "))
                v = float(input("Enter the velocity v of the spaceship as a fraction of c: "))
                if x < 0 or v < 0 or v > 1:
                    raise ValueError("Both x and v must be greater than zero and v cannot exceed c")
                break
            except ValueError as ve:
                print(ve)

    else:
        x = float(sys.argv[1])
        v = float(sys.argv[2])
        if x < 0 or v < 0 or v > 1:
            raise ValueError("Both x and v must be greater than zero and v cannot exceed c")
            sys.exit(1)
    
    t_rel, t_prop = compute_t(x, v)
    
    print("For the given x and v, %.3f years has passed on Earth, while %.3f years has\
          passed on the spaceship" % (t_rel, t_prop))