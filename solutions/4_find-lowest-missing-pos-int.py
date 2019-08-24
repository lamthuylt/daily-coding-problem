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
    We have to check at most n+1 numbers (from 1 to n+1) for an array of size n. 
    '''
    missing = 1
    for num in arr:
        if missing == num:
            missing += 1
    return missing



def lowest_positive_missing_2(arr):
    '''
    Method 2 - O(nLogn) 
    We firstly sort the array (O(nLogn)) then do a linear scan to search for the lowest positive integer missing (O(n)). 
    '''    
    sorted_arr = merge_sort(arr)            
    missing = 1
    index = 0
    while index < len(sorted_arr):
        if missing == sorted_arr[index]:
            missing += 1
        index += 1        
    return missing


'''
Merge sort
'''
def merge(L,R):
    # merge two sorted sublists (Left and Right) into one sorted list
    nL = len(L)
    nR = len(R)
    A = []
    i = j = 0
    # compare each pair of element of the two sublists to sort and merge them 
    while i<nL and j<nR:
        if L[i] <= R[j]:
            A.append(L[i])
            i += 1
        else:
            A.append(R[j])
            j += 1
    # when one sublist exhaust first, fill A with all the remaining elements of the other sublist
    if i == nL:
        A.extend(R[j:])
    elif j == nR:                
        A.extend(L[i:])        
    return A
        

def merge_sort(A):
    ''' O(nLogn) '''
    n = len(A)
    if n <= 1:
        return A
    else:
        mid = int(n/2)
        L = merge_sort(A[:mid])
        R = merge_sort(A[mid:])
        return merge(L,R)
    
if __name__ == "__main__":
    arr = [3, 4, -1, 1]
    print('Method 1: {}'.format(lowest_positive_missing_1(arr)))
    print('Method 2: {}'.format(lowest_positive_missing_2(arr)))
    
    
    