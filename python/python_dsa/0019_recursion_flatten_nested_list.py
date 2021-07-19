def flatten(lst):
    result = []
    for element in lst:
        if type(element) is list:
            result.extend(flatten(element))
        else:
            result.append(element)
    return result

print(flatten([[1],2,[3,4],5,[6,7,[8,9]]]))
