"""Module for reading opcodes"""

def opcodes(path):
    """method to read opcodes from a file
    path: path to the file to be read
    """

    with open(path, 'r') as fp:
        line = fp.readline()
        ops = [int(x) for x in line.split(',') if x != '']

    for i in range(0, len(ops), 4):
        if ops[i] == 99:
            break
        idx1 = ops[i + 1]
        idx2 = ops[i + 2]
        idx3 = ops[i + 3]
        if ops[i] == 1:
            ops[idx3] = ops[idx1] + ops[idx2]
        elif ops[i] == 2:
            ops[idx3] = ops[idx1] * ops[idx2]
        else:
            print('Something went wrong')
    print(ops)
