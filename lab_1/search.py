def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search(data, target, left, right):
    if right >= left:
        mid = (right + left) // 2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            return binary_search(data, target, left, mid - 1)
        else:
            return binary_search(data, target, mid + 1, right)
    else:
        return -1
