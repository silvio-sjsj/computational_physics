#! python3
# Usage: python3 exrc_2-2_h_satellite.py <orbital_period>, where the argument
# <orbital_period> is the desired orbital period of the satellite in seconds.
# If no arguments are given in command line, then the program # will asks for the user 
# to input that values.

"""
Exercise 2.2: Altitude of a satellite.

A satellite is to be launched into a circular orbit around the Earth so that it orbits 
the planet once every T seconds.

The program will compute the height of the satellite above the ground using the
following expression:
h = (G*M*T^2/4*pi^2)^(1/3) - R with a frame of reference that has h = 0 at the ground 
level and points from the ground up.
"""

import sys
from math import pow
from math import pi

G = 6.67e-11 # Newton's Gravitational constant in SI units
M = 5.97e24  # Is the Mass of the Earth in kg
R = 6371e3   # is the Earth's radius in m

def satellite_height(T):
    h = pow(((G*M*T**2)/(4*pi**2)), 1/3) - R
    return h

if __name__ == "__main__":
    if len(sys.argv) != 2:
        
        while True:
            try:
                T = float(input("Enter the desired value of the orbital period T in seconds > 0: "))
                if T < 0:
                    raise ValueError("T must be greater than zero")
                break
            except ValueError as ve:
                print(ve)

    else:
        T = float(sys.argv[1])
        if T < 0:
            raise ValueError("T must be greater than zero")
            sys.exit(1)

    h = satellite_height(T)
    
    print("The altitude of the satellit for the given T is: %.3f m" % h)

"""c) Use your program to calculate the altitudes of satellites that orbit the Earth 
once a day (so-called "geosynchronous" orbit), once every 90 minutes, and once every
45 minutes. What do you conclude from the last of these calculations?

- once a day: 24h -> 86400s -> h = 35855910.176 m = 35856 km
- every 90 minutes: 5400s -> h = 279321.625 m = 279.322 km
- every 45 minutes: 2700s -> h = -2181559.898 m < 0: the satellite won't enter orbit,
and it will fall back because its orbital velocity is less than the escape velocity
"""

"""d) Technically a geosynchronous satellite is one that orbits the Earth once per sidereal
day, which is 23.93 hours, not 24 hours. Why is this? And how much difference
will it make to the altitude of the satellite?

h(86400) - h(86148) = 82.148 km
"""