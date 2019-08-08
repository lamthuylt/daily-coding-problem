<script type="text/javascript"src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

\\[ {x}_{1,2}=\frac{-b\pm \sqrt{{b}^{2}-4ac}}{2a} \\]


# Sorting algorithms

### Bubble sort

This algorithm consists in repeatedly scanning through the list, and swapping each pair of adjacent elements if they are not in the right order (increasing or decreasing to be defined). This procedure is repeated until no more swap is required, meaning that the array is sorted. The name "bubble" comes from the way larger or smaller ellements bubble up to the top of the list.

Example:

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
	    if arr[i] > arr[i+1]:   # swap each pair of adjacent elements if they are not in increasing order
	    temp = arr[i]
	    arr[i] = arr[i+1]
	    arr[i+1] = temp
	    flag = 0
	if flag == 1:               # if we go through a pass without swapping, the array is already sorted
	    break
	return arr
```

* Time complexity: O($ n^2 $)
* Space complexity: in-place
 
### Insertion sort

<figure class="image">
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif" alt="{{ include description }}">
  figure source: https://en.wikipedia.org/wiki/Insertion_sort
</figure>

