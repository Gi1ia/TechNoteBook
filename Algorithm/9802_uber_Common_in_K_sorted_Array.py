def common_elements(sorted_array):
    if not sorted_array:
        return []
    
    N = len(sorted_array)
    if N == 1:
        return sorted_array[0]
    elif N == 2:
        return _find_common(sorted_array[0], sorted_array[1])
    else:
        left = common_elements(sorted_array[:2])
        right = common_elements(sorted_array[2:])
        return _find_common(left, right)
    

def _find_common(list1, list2):
    if not list1 or not list2:
        return []

    i, j = 0, 0
    res = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            res.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    
    return res

test1 = [[1, 2, 3, 40], [2, 3, 6], [2, 3, 6, 8]]
test2 = [[], [], [1]]
test3 = [[1, 2, 3, 40],[1, 2, 3, 40],[1, 2, 3, 40],[1, 2, 3, 40]]
print(common_elements(test3))