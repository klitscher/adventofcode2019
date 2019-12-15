"""Code for 1st advent challenge"""

def findfuelreqs():
    """function to calculate the the fuel reqs for the shuttle"""
    li = []
    with open('./day_1_input', 'r') as f:
        line = f.readline()
        li.append(int(line))
        while line:
            line = f.readline()
            if line is not '':
                li.append(int(line))

    for i in range(len(li)):
        li[i] = int(li[i]/3) - 2

    print(sum(li))
        
