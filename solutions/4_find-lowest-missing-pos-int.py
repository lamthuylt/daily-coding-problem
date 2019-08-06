"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""



def lowest_positive_missing_1(arr):
    '''
    Method 1 - O(n^2)    
    Check all positive integers, starting from 1, if it is the lowest value missing from the array. 
    We have to check at most n+1 numbers for an array of size n. 
    '''
    missing = 1
    for num in arr:
        if missing == num:
            missing += 1
    return missing
    




def lowest_positive_missing_2(arr):
    '''
    Method 2 - O(nlogn) 
    We use sorting beforehand (O(nlogn)) then do a linear scan of the array (O(n)). 
    '''
    def sort_array(arr):
        return arr
            
    sorted_arr = sort_array(arr)            
    missing = 1
    index = 0
    while index < len(sorted_arr):
        if missing == sorted_arr[index]:
            missing += 1
        index += 1        
    return missing




    
if __name__ == "__main__":
    arr = [3, 4, -1, 1]
    arr = [1, 2, 0]
    arr = [-1, -1, 2, 5]
    print('Method 1: {}'.format(lowest_positive_missing_1(arr)))
    print('Method 2: {}'.format(lowest_positive_missing_2(arr)))
    
    