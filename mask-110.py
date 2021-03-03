def getColsAndRows(inputStr):
    status = False
    if '*' in inputStr:
        rows = int(inputStr.split('*')[-1])
        cols = int(inputStr.split('*')[0])
        status = True
    elif inputStr.isdigit():
        rows = int(inputStr)
        cols = int(inputStr)
        status = True
    if status:
        return [cols, rows]


def getMaskSeven(num):
    ranges = getColsAndRows(num)
    if ranges:
        mask = ''
        for y in range(ranges[-1]):
            for x in range(ranges[0]):
                if ((x * y) % 2 + (x * y) % 3) % 2 == 0:
                    item = ' @'
                else:
                    item = '  '
                mask += item
            mask += '\n'
        return mask
    else:
        return 'Data is undefined'


print(getMaskSeven(input('Введите размеры маски через звёздочку (х*у): ')))
