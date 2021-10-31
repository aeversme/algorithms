from random import randint

input_array = [randint(0, 100) for i in range(8)]
merge_counter = 0


def mergesort(array):
    """
    Takes an array of unsorted integers and returns an array of sorted integers. 
    :param array: 
    :return: 
    """
    if len(array) < 2:
        return array
    else:
        half = len(array) // 2
        a = mergesort(array[:half])
        b = mergesort(array[half:])
    return merge(a, b)


def merge(array1, array2):
    """
    Takes two sorted arrays and returns a sorted array that is a merge of the two input arrays.
    :param array1:
    :param array2:
    :return:
    """
    global merge_counter
    merge_counter += 1
    i = 0
    j = 0
    sorted_array = []
    print(f"{merge_counter}: merging {array1} with {array2}")
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            sorted_array.append(array1[i])
            i += 1
        else:
            sorted_array.append(array2[j])
            j += 1
    sorted_array += array1[i:]
    sorted_array += array2[j:]
    return sorted_array


print(mergesort(input_array))
