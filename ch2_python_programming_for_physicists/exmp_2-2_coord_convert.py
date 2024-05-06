#! python3
# Usage: python3 exmp_2-2_coord_convert.py <coordinate_1> <coordinate_2> <input_coord>,
# where <coordinate_1> and <coordinate_2> are the coordinates to be converted, and
# <input_coord> is the coordinate scheme of the inputs, that is cartesian or polar.
# Given the coordinates and the scheme as inputs, the program will convert it to the
# other coordinate scheme, that is cartesian to polar or polar to cartesian.
# If no arguments are given in command line, then the program
# will asks for the user to input those values.

"""
Example 2.2: Converting polar coordinates - example from the book with imrpovements.

Suppose the position of a point in two-dimensional space is given to us in polar
coordinates r, θ and we want to convert it to Cartesian coordinates x, y. How
would we write a program to do this? The appropriate steps are:

1. Get the user to enter the values of r and θ.
2. Convert those values to Cartesian coordinates using the standard formu-
las:
    x = rcos(θ) , y = rsin(θ).
3. Print out the results.

In this program I also added the possibility of chosing to convert form polar
to cartesian coordinates.
"""

import sys
from math import sin, cos, pi, sqrt, atan, pow

def convert_to_cartesian(r, theta):
    
    x = r*cos(theta*pi/180)
    y = r*sin(theta*pi/180)

    return x, y

def convert_to_polar(x, y):
    
    r = sqrt(pow(x, 2) + pow(y, 2))
    theta = (atan(y/x))*180/pi

    return r, theta

if __name__ == "__main__":
    if len(sys.argv) != 4:

        conv = input("Your input is in polar or cartesian? chose p or c: ")

        if conv == 'c':
            try:
                x = float(input("Enter the x coordinate: "))
                y = float(input("Enter the y coordinate: "))       
            except ValueError as ve:
                print(ve)
            pol_r, pol_t = convert_to_polar(x, y)
            print("For the given x and y coordinates, the polar coordinates are: r = %.3f, θ = %.3fº" % (pol_r, pol_t))    

        else:
            while True:
                try:
                    r = float(input("Enter the radius r > 0: "))
                    theta = float(input("Enter the angle in degrees: "))
                    if r < 0:
                        raise ValueError("Radius must be greater than zero")
                    break
                except ValueError as ve:
                    print(ve)
            cart_x, cart_y = convert_to_cartesian(r, theta)
            print("For the given radius and angle θ, the cartesian coordinates are: x = %.3f, y = %.3f" % (cart_x, cart_y))

    else:
        conv = sys.argv[3]
        
        if conv == 'c':
            x = float(sys.argv[1])
            y = float(sys.argv[2])
            pol_r, pol_t = convert_to_polar(x, y)
            print("For the given x and y coordinates, the polar coordinates are: r = %.3f, θ = %.3fº" % (pol_r, pol_t))    

        else:
            r = float(sys.argv[1])
            theta = float(sys.argv[2])
            if r < 0:
                raise ValueError("Radius must be greater than zero")
                sys.exit(1)
            cart_x, cart_y = convert_to_cartesian(r, theta)
            print("For the given radius and angle θ, the cartesian coordinates are: x = %.3f, y = %.3f" % (cart_x, cart_y))