def insertion_sort(to_sort):
    result = []
    for element in to_sort:
        if not result:
            result.append(element)
        else:
            for index, result_element in enumerate(result):
                if element <= result_element:
                    result.insert(index, element)
                    break
            else:
                result.append(element)

    return result
