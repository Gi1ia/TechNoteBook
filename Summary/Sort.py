def quick_sort(nums):
    if len(nums) < 2:
        return nums

    pivot = nums[0]
    smaller = [x for x in nums[1:] if x <= pivot]
    larger = [x for x in nums[1:] if x > pivot]
    return quick_sort(smaller) + [pivot] + quick_sort(larger)

def merge_sort(ll):
	if len(ll) < 2:
		return ll
	num = int(len(ll)/2)
	left = merge_sort(ll[:num])
	right = merge_sort(ll[num:])
	return merge_aux(left, right)

def merge_aux(left, right):
	'''
	Merge left and right
	'''
	l = r = 0
	result = []
	while l<len(left) and r<len(right):
		if left[l] < right[r]:
			result.append(left[l])
			l += 1
		else:
			result.append(right[r])
			r += 1
		
		result += left[l:]
		result += right[r:]
		return result

def bubble_sort(l):
	n = len(l)
	for i in range(n):
		for j in range(1, n-i):
			if l[j - 1] > l[j]:
				l[j-1], l[j] = l[j], l[j-1]
	return l

def insert(l):
	n = len(l)
	for i in range(1, n):
		if l[i] < l[i-1]:
			temp = l[i]
			index = i
			for j in range(i-1, -1, -1):
				if l[j]>temp:
					l[j + 1] = l[j]
					index = j
				else:
					break
			l[index] = temp
	return l