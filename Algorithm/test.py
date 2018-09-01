import collections
tasks = [1, 1, 1, 2, 3, 3, 4, 5, 5, 5, 5, 5, 6]
tasks2 = ["a", 'a', 'a', 'b', 'b', 'c', 'c', 'c']
c = collections.Counter(tasks2)
print(c)

print(c.most_common(1))