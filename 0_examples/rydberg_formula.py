"""Atomic Physics Calculation: Rydberg Formula
https://en.wikipedia.org/wiki/Rydberg_formula

For a given value of m, the wavelengths lambda given by this formula
for all n > m form a series, the first three such series, for m = 1, 2, and 3,
being known as the Lyman, Balmer, and Paschen series, after their respective
discoverers.

In the formula below, n_1 is the principal quantum number of the lower energy level, and n_2
is the principal quantum number of the higher energy level for the atomic electron transition.
"""

R = 1.097e-2 # Rydberg constant

n_1 = int(input("Give the lower energy level (start of the series): "))
n_2 = int(input("Give the higher energy level: "))
n_max = int(input("How many terms of the series to calculate? "))

for m in range(n_1, n_2+1):
    print("Series for n_1 = ", m)
    for n in range(m+1, m+n_max+1):
        inv_lambda = R*(1/m**2-1/n**2)
        print("  ", 1/inv_lambda, "nm")