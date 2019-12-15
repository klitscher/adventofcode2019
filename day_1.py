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

    modulemass = sum(li)
    fuelmass = []
    for i in range(len(li)):
        num = li[i]
        while num > 0:
            num = int(num/3) - 2
            if num > 0:
                fuelmass.append(num)
    
    print(modulemass + sum(fuelmass))
