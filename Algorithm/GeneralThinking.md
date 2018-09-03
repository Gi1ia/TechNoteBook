# Overflow
# Compare float

# Bit Manipulating
## x&(-x)  lowest (right) significant bit
## x&(x - 1) clear lowest significant bit

# Tricks
## generate all valid transformations
### from 127
    ```
    front = wordDict & (set(word[:index] + ch + word[index+1:] for word in front 
        for index in range(len(beginWord)) for ch in 'abcdefghijklmnopqrstuvwxyz'))
    ```

    ```
    >>> sorted(x.items(), key=lambda pair: pair[1], reverse=True)
    [('c', 7), ('a', 5), ('b', 3)]
    ```
## Counter
```
task_counts = collections.Counter(tasks).values()
```
```
d = collections.Counter(tasks)
        counts = d.values()
        longest = max(counts)
```

## Heap
### custom comparator
The way to customize the heap order is to have each element on the heap to be a tuple, with the first tuple element being one that accepts normal Python comparisons.
### Example
```
li = [5, 7, 9, 1, 3] # initializing list
heapq.heapify(li) # using heapify to convert list into heap
```
