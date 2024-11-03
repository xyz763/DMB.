import random

def quick_sort(arr, left, right):
    if left < right:
        pivot_index = random.randint(left, right)
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        partition = partition_it(arr, left, right)
        quick_sort(arr, left, partition - 1)
        quick_sort(arr, partition + 1, right)

def partition_it(arr, left, right):
    pivot = arr[right]
    left_ptr = left - 1
    for i in range(left, right):
        if arr[i] < pivot:
            left_ptr += 1
            arr[left_ptr], arr[i] = arr[i], arr[left_ptr]
    arr[left_ptr + 1], arr[right] = arr[right], arr[left_ptr + 1]
    return left_ptr + 1

def print_array(arr):
    return " ".join(map(str, arr))

if __name__ == "__main__":
    arr = random.sample(range(100), 10)
    print("Original Array:\n" + print_array(arr))
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted Array:\n" + print_array(arr))