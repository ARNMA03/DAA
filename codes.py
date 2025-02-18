# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to detect if any swapping was done
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
                swapped = True
        # If no two elements were swapped in the inner loop, the array is sorted
        if not swapped:
            break
    return arr

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in unsorted part
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
if __name__ == "__main__":
    arr_bubble = [64, 34, 25, 12, 22, 11, 90]
    arr_selection = [64, 34, 25, 12, 22, 11, 90]
    arr_insertion = [64, 34, 25, 12, 22, 11, 90]

    print("Bubble Sort:", bubble_sort(arr_bubble))
    print("Selection Sort:", selection_sort(arr_selection))
    print("Insertion Sort:", insertion_sort(arr_insertion))