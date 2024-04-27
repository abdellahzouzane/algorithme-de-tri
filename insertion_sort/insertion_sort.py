from visualize import visualize_sorting


def insertion_sort(arr):
    n = len(arr)

    if n <= 1:
        return

    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            visualize_sorting(arr)
            j -= 1
        arr[j+1] = key
        visualize_sorting(arr)
    return arr
