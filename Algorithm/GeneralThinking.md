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
