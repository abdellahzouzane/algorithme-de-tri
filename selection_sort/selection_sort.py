from visualize import visualize_sorting


def selection_sort(arr):
    for i in range(len(arr)):
        zoro = i
        for j in range(i + 1, len(arr)):
            if arr[zoro] > arr[j]:
                zoro = j
        arr[i], arr[zoro] = arr[zoro], arr[i]
        visualize_sorting(arr)

    return arr
