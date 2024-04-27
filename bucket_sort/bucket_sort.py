from visualize import visualize_sorting


def bucket_sort(arr):
    for i in range(1, len(arr)):
        var = arr[i]
        visualize_sorting(arr)
        j = i - 1
        while (j >= 0 and var < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = var

    return (arr)
