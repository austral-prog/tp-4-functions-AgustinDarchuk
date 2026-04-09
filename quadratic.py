# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    if (b**2 + (-4 *a *c)) > 0:
        raiz1 = (-b + (b**2 -4 *a *c)**0.5) / (2*a)
        raiz2 = (-b - (b**2 -4 *a *c)**0.5) / (2*a)
        return f"({raiz1}, {raiz2})"
    if (b**2 + (-4 *a *c)) == 0: 
        raiz3 = - b / (2 * a)
        return f"({raiz3})"
    else:
        return f"( )"


def value_y(a, b, c, x):
    y = a * x **2 + b * x + c
    return y


def to_string(a, b, c):
    if a != 0 and b != 0 and c != 0:
        funcion = f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a != 0 and b != 0 and c == 0:
        funcion = f"f(x) = {a} * X^2 + {b} * X"
    elif a != 0 and b == 0 and c != 0:
        funcion = f"f(x) = {a} * X^2 + {c}"
    elif a == 0 and b == 0 and c == 0:
        funcion = f"f(x) = 0"
    elif a == 0 and b != 0 and c != 0:
        funcion = f"f(x) = {b} * X + {c}"
    elif a == 0 and b != 0 and c == 0:
        funcion = f"f(x) = {b} * X"
    elif a == 0 and b == 0 and c != 0:
        funcion = f"f(x) = {c}"
    return funcion

def derivation(a, b, c):
    derivada = f"f'(x) = {2 * a} * X + {b}"
    if a != 0 and b != 0:
        return derivada
    elif a != 0 and b == 0:
        derivada = f"f'(x) = {2 * a} * X"
        return derivada
    elif a == 0 and b != 0:
        derivada = f"f'(x) = {b}"
        return derivada
    elif a == 0 and b == 0:
        derivada = f"f'(x) = 0"
        return derivada
    



