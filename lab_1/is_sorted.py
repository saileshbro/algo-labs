def is_sorted(array):
    temp = array[:]
    temp.sort()
    if(array == temp):
        return True
    return False
