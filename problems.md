# Index
- [x] [#1 Check pair sum up to a value](#problem-1-easy) [[solution]](solutions/1_check-sum-pair-in-array.py)
- [x] [#2 Product array](#problem-2-hard) [[solution]](solutions/2_product-array.py)
- [x] [#3 Serialize deserialize binary tree](#problem-3-medium) [[solution]](solutions/3_serialize-deserialize-binary-tree.py)
- [x] [#4 Find the lowest missing positive int](#problem-4-hard) [[solution]](solutions/4_find-lowest-missing-pos-int.py)
- [ ] [#5 Functional programming](#problem-5-medium)
- [ ] [#6 XOR linked list](#problem-6-hard)
- [x] [#7 Decode message](#problem-7-medium) [[solution]](solutions/7_decode-message.py)
- [x] [#8 Count unival subtrees](#problem-8-easy) [[solution]](solutions/8_count-unival-subtrees.py)
- [ ] [#9 Largest non adjacent sum](#problem-9-hard)
- [ ] [#10 Job schedular](#problem-10-medium)
- [x] [#11 Autocomplete system](#problem-11-medium) [[solution]](solutions/11_autocomplete-system.py)
- [ ] [#12 Count ways to count staircase](#problem-12-hard) 
- [ ] [#13 Longest substring with k distinct characters](#problem-13-hard) 
- [x] [#14 Estimate pi using Monte Carlo method](#problem-14-medium) [[solution]](solutions/14_estimate-pi-Monte-Carlo.py)
- [ ] [#15 Random pick from out of memory stream](#problem-15-medium)
- [x] [#16 Record orders in a log](#problem-16-easy) [[solution]](solutions/16_order-log.py)
- [ ] [#17](#problem-17-hard) 
- [ ]


# Problem description

### Problem #1 [Easy] 
This problem was recently asked by Google.\
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.\
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.\
Bonus: Can you do this in one pass?

### Problem #2 [Hard] 
This problem was asked by Uber.\
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.\
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].\
Follow-up: what if you can't use division?

### Problem #3 [Medium] 
This problem was asked by Google.\
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.\
For example, given the following Node class
```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
The following test should pass:
```python
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```

### Problem #4 [Hard]
This problem was asked by Stripe.\
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.\
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

### Problem #5 [Medium]
This problem was asked by Jane Street.\
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.\
Given this implementation of cons:
```python
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```
Implement car and cdr.

### Problem #6 [Hard]
This problem was asked by Google.\
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.\
If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

### Problem #7 [Medium]
This problem was asked by Facebook.\
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.\
You can assume that the messages are decodable. For example, '001' is not allowed.

### Problem #8 [Easy] 
This problem was asked by Google.\
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.\
For example, the following tree has 5 unival subtrees:
```
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
```

### Problem #9 [Hard]
This problem was asked by Airbnb.\
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be `0` or negative.\
For example, `[2, 4, 6, 2, 5]` should return `13`, since we pick `2`, `6`, and `5`. `[5, 1, 1, 5]` should return `10`, since we pick `5` and `5`.\
Follow-up: Can you do this in O(N) time and constant space?

### Problem #10 [Medium]
This problem was asked by Apple.\
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

### Problem #11 [Medium]
This problem was asked by Twitter.\
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have `s` as a prefix.
For example, given the query string `de` and the set of strings [`dog`, `deer`, `deal`], return [`deer`, `deal`].\
Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.


### Problem #12 [Hard]
This problem was asked by Amazon.\
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.\
For example, if N is 4, then there are 5 unique ways:
* 1, 1, 1, 1
* 2, 1, 1
* 1, 2, 1
* 1, 1, 2
* 2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.


### Problem #13 [Hard]
This problem was asked by Amazon.\
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.\
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


### Problem #14 [Medium]
This problem was asked by Google.\
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.\
Hint: The basic equation of a circle is x^2 + y^2 = r^2.


### Problem #15 [Medium]
This problem was asked by Facebook.\
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.


### Problem #16 [Easy]
This problem was asked by Twitter.\
You run an e-commerce website and want to record the last `N order` ids in a log. Implement a data structure to accomplish this, with the following API:
* record(order_id): adds the order_id to the log
* get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.


### Problem #17 [Hard]
This problem was asked by Google.\
Suppose we represent our file system by a string in the following manner:\

The string `"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"` represents:
```
dir
    subdir1
    subdir2
        file.ext
```
The directory `dir` contains an empty sub-directory `subdir1` and a sub-directory `subdir2` containing a file `file.ext`.\
The string `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"` represents:
```
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
```
The directory `dir` contains two sub-directories `subdir1` and `subdir2`. `subdir1` contains a file `file1.ext` and an empty second-level sub-directory `subsubdir1`. `subdir2` contains a second-level sub-directory `subsubdir2` containing a file `file2.ext`.\
We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is `"dir/subdir2/subsubdir2/file2.ext"`, and its length is 32 (not including the double quotes).\
Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.\
Note:
* The name of a file contains at least a period and an extension.
* The name of a directory or sub-directory will not contain a period.