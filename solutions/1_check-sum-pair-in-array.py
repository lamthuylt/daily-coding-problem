"""
This problem was asked by Google.    

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
# O(n^2)
def check_sum_pair(liste, k):
    diffs = []
    for num in liste:
        if num in diffs:
            return True
        else:
            diffs.append(k-num)
    return False

# O(n)
def check_sum_pair_2(liste, k):
    diffs = {}
    for num in liste:
        # num in diffs => O(1)
        # num in diffs.keys() => O(n)
        if num in diffs:
            return True
        else:
            diffs[k-num] = 1
    return False


if __name__ == '__main__':
    liste = [5, -15, 3, 7]
    k = 10
    print('Check sum method 1: {}'.format(check_sum_pair(liste,k)))
    print('Check sum method 2: {}'.format(check_sum_pair_2(liste,k)))