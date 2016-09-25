from matplotlib import pyplot

def step_function(x, a=0):
    if (x - a) > 0:
        return 1
    else:
        return 0
