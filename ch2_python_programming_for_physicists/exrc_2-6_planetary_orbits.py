#! python3
# Usage: python3 exrc_2-6_planetary_orbits.py <distance> <velocity>, where <distance>
# and <velocity> are the distance in m of a planet to the Sun and its velocity at the
# perihelion in m/s, respectively. Given these two informations, the program computes
# the distance and velocity at the aphelion as well as the body's orbital period in
# years and its orbital eccentricity.
# If no arguments are given in command line, then the program
# will asks for the user to input those values.

""""
Exercise 2.6: Planetary orbits: The orbit in space of one body around another, such as
a planet around the Sun, need not be circular. In general it takes the form of an
ellipse, with the body sometimes closer in and sometimes further out. If you are given
the distance l1 of closest approach that a planet makes to the Sun, also called its
perilrelion, and its linear velocity v1 at perihelion, then any other property of the
orbit can be calculated from these two as follows.
"""

import sys
import numpy as np
from math import sqrt
from math import pi

G = 6.6738e-11 # Gravitational constant in SI units
M = 1.9891e30  # Mass os the Sun in kg

def compute_v2(l1, v1):
    "Compute the velocity v2 through its quadratic equation finding the smaller root"
    a = 1
    b = (-2*G*M)/(v1*l1)
    c = -(v1**2 - (2*G*M)/(l1))
    roots = np.array([((-b + sqrt(b**2 - 4*a*c))/2*a), ((-b - sqrt(b**2 - 4*a*c))/2*a)])
    v2 = np.min(roots)

    return v2

def compute_l2(l1, v1, v2):
    "Compute the aphelion distance and convert from m to km"

    l2 = ((l1*v1)/v2)/1000

    return l2

def compute_axis(l1, l2):
    """Computes the semi-major axis and the semi-minor axis"""

    a_axis = (l1 + l2)/2
    b_axis = sqrt(abs(l1*l2))

    return a_axis, b_axis

def compute_orbital_period(a_axis, b_axis, l1, v1):
    "Compute the oribtal period given the semi axis and the perihelion parameters"

    T = (2*pi*a_axis*b_axis)/(l1*v1)

    return T

def compute_orbital_eccentricity(l1, l2):
    "Computes the orbital eccentricity given the perihelion and aphelion distances"

    e = (l2 - l1)/(l2 + l1)

    return e

def seconds_to_years(seconds):
    "Convert the orbital period from seconds to years"

    seconds_in_year = 365.25 * 24 * 60 * 60
    years = seconds / seconds_in_year

    return years


if __name__ == "__main__":
    if len(sys.argv) != 3:
        
        while True:
            try:
                l1 = float(input("Enter the perihelion distance l1 to the sun in meters: "))
                v1 = float(input("Enter the velocity v at the perihelion in meters per seconds: "))
                if l1 < 0 or v1 < 0:
                    raise ValueError("Both l1 and v must be greater than zero")
                break
            except ValueError as ve:
                print(ve)

    else:
        l1 = float(sys.argv[1])
        v1 = float(sys.argv[2])
        if l1 < 0 or v1 < 0:
            raise ValueError("Both l1 and v must be greater than zero.")
            sys.exit(1)
    
    v2 = compute_v2(l1, v1)
    l2 = compute_l2(l1, v1, v2)
    a_axis, b_axis = compute_axis(l1, l2)
    T = compute_orbital_period(a_axis, b_axis, l1, v1)
    T = seconds_to_years(T)
    e = compute_orbital_eccentricity(l1, l2)
    
    print("For the given perihelion distance and velocity")
    print("The aphelion distance is: %.3f km" %l2)
    print("The velocity at the aphelion is: %.3f m/s" %v2)
    print("The orbital period is: %.3f years" %T)
    print("The orbital eccentricity is: %.3f " %e)