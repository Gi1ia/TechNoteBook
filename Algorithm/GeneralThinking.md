# Overflow
# Compare float

# Bit Manipulating
## x&(-x)  lowest (right) significant bit
This could be used in Binary Index
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

## Represent a graph
 1. Give number of nodes, and all edges
 2. Give a list, on each index, 

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
# Python List Slice
```
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
##########
a[start:end:step] # start through not past end, by step
a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
```

## difaultdict()
```
>>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d = defaultdict(list)
>>> for k, v in s:
...     d[k].append(v)
...
>>> sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```
```
>>> d = {}
>>> for k, v in s:
...     d.setdefault(k, []).append(v)
...
>>> sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```

## Set
If you want to use set, consider duplication first! (No. 76)
Set is easy to lost track of duplicated elements in different places.

## Zip()
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> list(zipped)
[(1, 4), (2, 5), (3, 6)]
>>> x2, y2 = zip(*zip(x, y))
>>> x == list(x2) and y == list(y2)
True

## Sort
* intervals.sort(key=lambda x: x.start) # python 2 ??
* intervals = sorted(intervals, key=lambda x: x.start)