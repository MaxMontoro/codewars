def solution(args):

    diff_is_one = lambda x: True if abs(x[0]-x[1]) == 1 else False
    output = ''
    in_a_row = []

    for index, item in enumerate(args):
        try:
            if diff_is_one((item, args[index+1])):
                in_a_row.append(item)
                in_a_row.append(args[index+1])
                continue
            else:
                if len(in_a_row) >= 3:
                    output += ',{}-{}'.format(in_a_row[0], in_a_row[-1])
                    in_a_row = []
                else:
                    if in_a_row:
                        output += ',' + ','.join([str(item) for item in in_a_row])
                        in_a_row = []
                    else:
                        output += ',' + str(item)
                        in_a_row = []
        except IndexError:
            if diff_is_one((item, args[index-1])):
                in_a_row.append(item)
            if len(set(in_a_row)) >= 3:
                output += ',{}-{}'.format(in_a_row[0], in_a_row[-1])
            elif len(set(in_a_row)) <= 3:
                if len(set(in_a_row)) == 2:
                    output += ',' + ','.join([str(item) for item in sorted(set(in_a_row))])
                    break
                output += ',' + str(item)
            else:
                output += ',' + str(item)
    output = output.lstrip(',')
    return output
