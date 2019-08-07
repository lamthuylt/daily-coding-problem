# Sorting algorithms

## Bubble sort
Bubble the largest element up to the highest index of the array, then bubble the second largest element up to the second highest index, and so on.

 <figure class="image">
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif" alt="{{ include description }}">
  figure source: https://en.wikipedia.org/wiki/Bubble_sort
</figure>




```python
def bubble_sort(arr):
    for k in range(len(arr)-1,0,-1):       
        flag = 1   
	print(arr)
	for i in range(k):
	    if arr[i] > arr[i+1]:   # swap the two adjacent elements if they are not increasingly sorted yet
	    temp = arr[i]
	    arr[i] = arr[i+1]
	    arr[i+1] = temp
	    flag = 0
	if flag == 1:               # if we go through a pass without swapping, the array is already sorted
	    break
	return arr
```
* Time complexity: O(n^2)
 
## Insertion sort

 <figure class="image">
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif" alt="{{ include description }}">
  figure source: https://en.wikipedia.org/wiki/Insertion_sort
</figure>

