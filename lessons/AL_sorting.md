# Sorting algorithms

### Bubble sort

This algorithm consists in repeatedly scanning through the list, comparing each pair of adjacent elements, and swapping them if they are in the wrong order. By this way, larger/smaller elements bubble up to the top of the list, which is the origin of the name "Bubble sort". This procedure is repeated until no more swap is required, meaning that the list is sorted. 

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

* Time complexity: O(n^2)
* Space complexity: in-place
 


### Selection sort

Example:
<figure class="image">
  <img src="https://algorithms.tutorialhorizon.com/selection-sort-java-implementation/selection-sort-gif/" alt="{{ include description }}">
  figure source: https://algorithms.tutorialhorizon.com/selection-sort-java-implementation/selection-sort-gif/
</figure>

```python
def selection_sort(arr):
    for i in range(len(arr)-1):                   
        # find index of minimum element from i till n-1
        iMin = i
        for j, num in enumerate(arr[i+1:]):                
            if num < arr[iMin]:
                iMin = i+j+1
        # swap ith element and minimum element 
        if iMin != i:
            temp = arr[i]
            arr[i] = arr[iMin]
            arr[iMin] = temp
        print(arr)
    return arr
```

* Time complexity: O(n^2)
* Space complexity: in-place




### Insertion sort

<figure class="image">
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif" alt="{{ include description }}">
  figure source: https://en.wikipedia.org/wiki/Insertion_sort
</figure>

