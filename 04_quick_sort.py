def sum_for(arr):
    total = 0
    # Iterate over each element in the array
    for x in arr:
        # Add each element to total
        total += x
    # Return the total sum
    return total


def sum_recursion(list):
    if not len(list):
        return 0
    # Return the sum of the first element and the sum of the rest of the list
    return list[0] + sum_recursion(list[1:])


def count(list):
    if not list:
        return 0
    # Return 1 plus the count of the rest of the list
    return 1 + count(list[1:])


def find_max(list):
    if len(list) == 2:
        return list[0] if list[0] >= list[1] else list[1]
    # Return the larger between the first element and the maximum of the rest of the list
    return list[0] if list[0] >= find_max(list[1:]) else find_max(list[1:])


def quick_sort(array):
    if len(array) < 2:
        # base case, arrays with 0 or 1 element are already "sorted"
        return array
    else:
        # Choose the first element as pivot
        pivot = array[0]
        # Create a sub-array of all the elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # Create a sub-array of all the elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]
        # Return the sorted array
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    print(sum_for([1, 2, 3, 4]))
    print(sum_recursion([1, 2, 3, 4]))
    print(count([1, 2, 3, 4]))
    print(find_max([1, 2, 3, 4]))
    print(quick_sort([10, 5, 2, 3]))
