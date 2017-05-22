def next_bigger(number):

    backwards = list(str(number))[::-1]
    pivot = False

    for index, digit in enumerate(backwards):
        if index != 0:
            previous = backwards[index -  1]
            if int(digit) < int(previous):
                pivot = len(str(number))-index-1
                break
    if pivot is False:
        return -1

    as_list = list(str(number))
    new_number = as_list[:pivot]
    swapped = [sorted([int(digit) for digit in as_list[pivot:] if int(digit) > int(as_list[pivot])])[0]]
    new_number += swapped
    last_part =  sorted([int(i) for i in as_list[pivot: ]])
    last_part.remove(int(swapped[0]))
    new_number += last_part
    return int(''.join([str(i) for i in new_number]))
