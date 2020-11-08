def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(array, p, r):
    if r-p > 1:
        q = (p+r)//2
        merge_sort(array, p, q)
        merge_sort(array, q, r)
        merge(array, p, q, r)


def merge(array, p, q, r):
    L = array[p:q]
    R = array[q:r]
    L.append(float("inf"))
    R.append(float("inf"))
    i = j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
