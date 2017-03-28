def insertion_sort(input):
    result = []
    for this_char in input:
        if not result:
            result.append(this_char)
        else:
            for index, result_char in enumerate(result):
                if this_char <= result_char:
                    result.insert(index, this_char)
                    break
            else:
                result.append(this_char)

    return result
