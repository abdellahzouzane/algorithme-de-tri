from visualize import visualize_sorting


def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        yaya = arr.pop()

    juju = []
    soso = []
    for san in arr:
        if san > yaya:
            juju.append(san)

        else:
            soso.append(san)
    visualize_sorting(arr)

    return quick_sort(soso) + [yaya] + quick_sort(juju)
