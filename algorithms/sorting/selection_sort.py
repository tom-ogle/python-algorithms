def selection_sort(to_sort):
    for i, element in enumerate(to_sort):
        minimum = i
        for j in range(i + 1, len(to_sort)):
            if to_sort[j] < to_sort[minimum]:
                minimum = j
        to_sort[minimum], to_sort[i] = to_sort[i], to_sort[minimum]
    return to_sort
