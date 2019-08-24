'''
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.
'''

import numpy as np

def estimate_pi(ndecimal):
    N_inside = 0
    N_total = 10**ndecimal
    # randomize points inside a 1x1 square such that whose coordinates follow uniform distribution    
    for i in range(N_total):        
        x = np.random.uniform()
        y = np.random.uniform()
        # count the number of points inside the quadrant of radius 1 inscribed in the unit square
        if x*x + y*y <= 1:
            N_inside += 1
    # the ratio between N_inside and N_total approximates the ratio between two areas, i.e. pi/4
    return 4*float(N_inside)/float(N_total)
    

if __name__ == "__main__":
    print(estimate_pi(3))
    
    
    
    
