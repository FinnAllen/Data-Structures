#Author: Finnian Allen

def Maximum(T):
    if len(T) == 1:
        return T[0]
    elif len(T) == 2:
        if T[0] >= T[1]:
            return T[0]
        else:
            return T[1]
    else: # T > 2
        return recurseMax(T, T[0])
    
def recurseMax(T, curMax):
    if len(T) != 0:
        if T[0] >= curMax:
            return recurseMax(T[1:], T[0])
        else:
            return recurseMax(T[1:], curMax)
    else:
        return curMax

def Remove(T, E):
    if len(T) == 0:
        return T
    elif len(T) == 1:
        return ()
    elif len == 2:
        if T[0] == E:
            return T[1]
        else:
            return T[0]
    else: 
        return T[:T.index(E)] + T[T.index(E) + 1:]

def Sort(T):
    if T:
        return Sort(Remove(T, Maximum(T))) + (Maximum(T),)
    else: # no elements in tuple
        return T
    
print(Maximum((1,)))                      #  1                            2 pt.
print(Maximum((-2, -1)))                  # -1                            2 pt.
print(Maximum((1, 1)))                    #  1                            2 pt.
print(Maximum((1, 2, 3)))                 #  3                            2 pt.

print(Remove((), 1))                      #  ()                           2 pt.
print(Remove((1,), 1))                    #  ()                           2 pt.
print(Remove((0, 1), 0))                  #  (1,)                         2 pt.
print(Remove((0, 1, 2, 1, 3), 1))         #  (0, 2, 1, 3)                 2 pt.
print(Remove((0, 1, 2, 1, 3), 2))         #  (0, 1, 1, 3)                 2 pt.
print(Remove((1, 2, 3), 3))               #  (1, 2)                       2 pt.

print(Sort(()))                           #  ()                           2 pt.
print(Sort((0,)))                         #  (0,)                         2 pt.
print(Sort((0, -1)))                      #  (-1, 0)                      2 pt.
print(Sort((1, 0)))                       #  (0, 1)                       2 pt.
print(Sort((0, 0, 1)))                    #  (0, 0, 1)                    2 pt.
print(Sort((0, -1, 0)))                   #  (-1, 0, 0)                   2 pt.
print(Sort((0, 0, 1)))                    #  (0, 0, 1)                    2 pt.

print(Sort((9, 8, 7, 6, 5, 4, 3, 2, 1)))  #  (1, 2, 3, 4, 5, 6, 7, 8, 9)  2 pt.
print(Sort((1, 2, 3, 4, 5, 6, 7, 8, 9)))  #  (1, 2, 3, 4, 5, 6, 7, 8, 9)  2 pt.
print(Sort((1, 2, 1, 4, 2, 5, 4, 5, 3)))  #  (1, 1, 2, 2, 3, 4, 4, 5, 5)  2 pt.












