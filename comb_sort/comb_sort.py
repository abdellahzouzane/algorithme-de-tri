from visualize import visualize_sorting


def comb_sort(arr):
    lolo = len(arr)
    swapped = True
    while lolo > 1 or swapped:
        lolo = max(1, int(lolo/1.35))
        swapped = False
        for i in range(len(arr)-lolo):
            j = i + lolo

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                visualize_sorting(arr)
                swapped = True
            visualize_sorting(arr)
    return arr
