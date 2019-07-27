"""
This problem was asked by Google.    

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def check_sum_pair(liste, k):
    diffs = []
    for num in liste:
        if num in diffs:
            return True
        else:
            diffs.append(k-num)
    return False

	
if __name__ == '__main__':
    liste = [10, -15, 3, 7]
    k = 17
    print('Check sum: {}'.format(check_sum_pair(liste,k)))