#! python3
# Usage: python3 exrc_2-5_quantum_pot_step.py <energy> <potential> <mass>, where
# <energy> is the particle's energy, <potential> is the potential step or barrier,
# and <mass> is the particle's mass as a multiple of the electron's mass (but it doesn't
# matter since the formula really doesn't depend on the mass at all).
# Given those variables the program checks for some conditions and then calcualtes the
# transmition and reflection probabilities.
# If no arguments are given in command line, then the program
# will asks for the user to input those values.

""""
Exercise 2.5: Quantum potential step. **With modifications**
A well-known quantum mechanics problem involves a particle of mass m that encoun-
ters a one-dimensional potential step.
The particle with initial kinetic energy E and wavevector k1 enters from the left and
encounters a sudden jump in potential energy of height V at position x = 0.
By solving the Schrtidinger equation, one can show that when E > V the particle may
either (a) pass the step, in which case it has a lower kinetic energy of E - V on the
other side and a correspondingly smaller wavevector of k2, or (b) it may be reflected,
keeping all of its kinetic energy and an unchanged wavevector but moving in the opposite
direction. The probabilities T and R for transmission and reflection are
given by

T = (4*k_1*k_2)/(k_1 + k_2)², R = (k_1 - k_2)²/(k_1 + k_2)²

Suppose we have a particle with mass equal to the electron mass and energy 1OeV
encountering a potential step of height 9eV. Write a Python program to compute and print
out the transmission and reflection probabilities using the formulas above.
"""

import sys
from math import sqrt

constant = 6.62607015e-34 # Planck's constant in SI units
m_e = 9.11e-31 # elecntron mass in SI units

def compute_wave_vectors(E, V, m):
    """Computes the wave vectors k_1 and k_2 given E, V and the mass m"""

    k_1 = sqrt(2*m*E)/constant
    k_2 = sqrt(2*m*(E-V))/constant

    return k_1, k_2

def comp_probabilities(k_1, k_2):
    """Computes the transmition and reflection probabilities for k_1 and k_2"""

    T = round(4*k_1*k_2/pow(k_1 + k_2, 2), 4)
    R = round(pow(k_1 - k_2, 2)/pow(k_1 + k_2, 2), 4)
    
    assert T + R == 1
    return R, T

if __name__ == "__main__":
    if len(sys.argv) != 4:
        
        while True:
            try:
                E = float(input("Enter the Energy E in eV: "))
                V = float(input("Enter the Potential step in eV with V < E: "))
                m = float(input("Enter the mass of the particle as a multiple of the mass of the electron in kg: "))
                if m < 0 or E < V:
                    raise ValueError("The mass must be greater than zero or we must have E > V")
                break
            except ValueError as ve:
                print(ve)

    else:
        E = float(sys.argv[1])
        V = float(sys.argv[2])
        m = float(sys.argv[3])
        if m < 0 or E < V:
            raise ValueError("The mass must be greater than zero or we must have E > V")
            sys.exit(1)
    
    m = m*m_e
    k_1, k_2 = compute_wave_vectors(E, V, m)
    R, T = comp_probabilities(k_1, k_2)
    
    print("For the given mass m, potential step V and energy E, the transmission probability is %.4f and\
        the reflection transmission is %.4f" % (T, R))