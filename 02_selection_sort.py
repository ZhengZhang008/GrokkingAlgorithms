# Finds the smallest value in an array
def find_smallest(arr):
    # Stores the smallest value
    smallest = arr[0]
    # Stores the index of the smallest value
    smallest_index = 0
    for i in range(1, len(arr)):
        # If the current element is smaller than the smallest found so far
        if arr[i] < smallest:
            # Update the smallest value and its index
            smallest = arr[i]
            smallest_index = i
    # Return the index of the smallest element
    return smallest_index


def selection_sort(arr):
    # Initialize a new array to store the sorted elements
    new_arr = []
    for i in range(len(arr)):
        # Finds the smallest element in the array
        smallest = find_smallest(arr)
        # Remove the smallest element from the original array and add it to the new array
        new_arr.append(arr.pop(smallest))
    # Return the sorted array
    return new_arr


if __name__ == "__main__":
    print(selection_sort([5, 3, 6, 2, 10]))
