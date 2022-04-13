def layout(lstlst, calculate):
    result = ["", "", "", ""]
    for lst in lstlst:
        result[0] = result[0] + lst[0] + '    '
        result[1] = result[1] + lst[1] + '    '
        result[2] = result[2] + lst[2] + '    '
        result[3] = result[3] + lst[3] + '    '

    for i in range(len(result)):
        result[i] = result[i].rstrip()

    if calculate == True:
        return '\n'.join(result)
    else:
        return '\n'.join(result[:len(result)-1])


def arithmetic_arranger(problems, calculate=False):
    if(len(problems) > 5):
        return 'Error: Too many problems.'
    result = list()
    for op in problems:
        res = op.split()
        resop = 0
        if res[1] == '-':
            try:
                resop = int(res[0]) - int(res[2])
            except ValueError:
                return ('Error: Numbers must only contain digits.')
        elif res[1] == '+':
            try:
                resop = int(res[0]) + int(res[2])
            except ValueError:
                return ('Error: Numbers must only contain digits.')
        else:
            return ('Error: Operator must be \'+\' or \'-\'.')
        max = 0
        if len(res[0]) > len(res[2]):
            max = len(res[0])
        else:
            max = len(res[2])
        if max > 4:
            return 'Error: Numbers cannot be more than four digits.'
        res[0] = res[0].rjust(max + 2, ' ')
        res[1] = res[1] + res[2].rjust(max + 1, ' ')
        res[2] = ''.rjust(max+2, '-')
        res.append(str(resop).rjust(max+2, ' '))
        result.append(res)
    return layout(result, calculate)