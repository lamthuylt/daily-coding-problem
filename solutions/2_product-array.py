"""
This problem was asked by Uber. 
   
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.  
  
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
    
Follow-up: what if you can't use division?
"""

import numpy as np

# O(n)
def product_usingDivision(array):
    product = 1
    nb_zero = 0
    index_zero = -1
    for i in range(len(array)):
        if array[i] != 0:
            product *= array[i]
        else:
            nb_zero += 1
            index_zero = i

    new_array = np.zeros(len(array))        # default case: multiple 0 in array
    if nb_zero == 0:                        # no 0 in array
        for i in range(len(array)):
            new_array[i] = product/array[i]
    elif nb_zero == 1:                      # case only one 0 in array
       new_array[index_zero] = product
    
    return new_array

# O(n^2)
def product_withoutDivision(array):
    new_array = np.ones(len(array))
    for i,num in enumerate(array):
        for j in range(len(new_array)):
            if j!=i:
                new_array[j] *= num
    return new_array

	
if __name__ == '__main__':
    array = [1, 2, 3, 4, 0]
    print('- Product using division: {}'.format(product_usingDivision(array)))
    print('- Product without division: {}'.format(product_withoutDivision(array)))