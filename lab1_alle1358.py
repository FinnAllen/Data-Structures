#Author: Finnian Allen
#Date Assigned: 9/10/2019

def isInside(v, e):
    if type(e) == tuple:
        if left(e) == v or right(e) == v:
            return True
        else:
            return isInside(v, left(e) or right(e))
    else:
        return v == e

def left(e):
    return e[0]

def op(e):
    return e[1]

def right(e):
    return e[2]

def solve(v, q):
    if isInside(v, left(q)): # our variable is on the left of the equation
        return solving(v, q)
    else: # our variable is on the right of the equation
        return solving(v, (right(q), op(q), left(q)))

def solving(v, q):
    if v == left(q):
        return q
    else:
        return dispatcher[op(left(q))](v, q) # this uses a dictionary like a switch to act a our dispatcher from class
    
def solvingAdd(v, q):
    A = left(left(q))
    B = right(left(q))
    C = right(q)
    if isInside(v, A):
        return solving(v, (A, '=', (C, '-', B)))
    elif isInside(v, B):
        return solving(v, (B, '=', (C, '-', A)))

def solvingSub(v, q):
    A = left(left(q))
    B = right(left(q))
    C = right(q)
    if isInside(v, A):
        return solving(v, (A, '=', (C, '+', B)))
    elif isInside(v, B):
        return solving(v, (B, '=', (A, '-', C)))

def solvingMul(v, q):
    A = left(left(q))
    B = right(left(q))
    C = right(q)
    if isInside(v, A):
        return solving(v, (A, '=', (C, '/', B)))
    elif isInside(v, B):
        return solving(v, (B, '=', (C, '/', A)))
    
def solvingDiv(v, q):
    A = left(left(q))
    B = right(left(q))
    C = right(q)
    if isInside(v, A):
        return solving(v, (A, '=', (C, '*', B)))
    elif isInside(v, B):
        return solving(v, (B, '=', (A, '/', C)))

dispatcher = { # dictionary as a switch statement
    "+" : solvingAdd,
    "-" : solvingSub,
    "*" : solvingMul,
    "/" : solvingDiv}

print(isInside('x', 'x'))                          #  True   1 point
print(isInside('x', 'y'))                          #  False  1 point
print(isInside('x', ('x', '+', 'y')))              #  True   2 points
print(isInside('x', ('a', '+', 'b')))              #  False  2 points
print(isInside('+', ('a', '+', 'b')))              #  False  2 points
print(isInside('x', (('m', '*', 'x'), '+', 'b')))  #  True   2 points

print(solve('x', (('a', '+', 'x'), '=', 'c')))
#  ('x', '=', ('c', '-', 'a'))  2 points

print(solve('x', (('x', '+', 'b'), '=', 'c')))
#  ('x', '=', ('c', '-', 'b'))  2 points

print(solve('x', (('a', '-', 'x'), '=', 'c')))
#  ('x', '=', ('a', '-', 'c'))  2 points

print(solve('x', (('x', '-', 'b'), '=', 'c')))
#  ('x', '=', ('c', '+', 'b'))  2 points

print(solve('x', (('a', '*', 'x'), '=', 'c')))
#  ('x', '=', ('c', '/', 'a'))  2 points

print(solve('x', (('x', '*', 'b'), '=', 'c')))
#  ('x', '=', ('c', '/', 'b'))  2 points

print(solve('x', (('a', '/', 'x'), '=', 'c')))
#  ('x', '=', ('a', '/', 'c'))  2 points

print(solve('x', (('x', '/', 'b'), '=', 'c')))
#  ('x', '=', ('c', '*', 'b'))  2 points

print(solve('y', ('y', '=', (('m', '*', 'x'), '+', 'b'))))
# ('y', '=', (('m', '*', 'x'), '+', 'b'))  2 points

print(solve('x', ('y', '=', (('m', '*', 'x'), '+', 'b'))))
# ('x', '=', (('y', '-', 'b'), '/', 'm'))  2 points

print(solve('a', (('b', '+', 'c'), '=', ('d', '*', (('a', '/', 'e'), '-', 'f')))))
# ('a', '=', (((('b', '+', 'c'), '/', 'd'), '+', 'f'), '*', 'e'))  5 points














