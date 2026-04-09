# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    # if x >= y:
    #     maximo = x
    # elif y > x:
    #     maximo = y
    
    maximo = max(x,y)
    return maximo


def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    maximo = max_of_two(x,y)
    maximo = max_of_two(maximo,z)
    return maximo
