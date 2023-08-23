# Finds the smallest value in an array
def find_smallest(arr):
    # Stores the smallest value
    smallest = arr[0]
    # Stores the index of the smallest value
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# Sort array
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        # Finds the smallest element in the array and adds it to the new array
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


if __name__ == "__main__":
    print(selection_sort([5, 3, 6, 2, 10]))
