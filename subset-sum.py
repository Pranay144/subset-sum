import random
L = random.sample(range(1,10001),1000)      # generate random list in the given range
L.sort(reverse=True)                        # sort in descending order
print(L)
S = sum(L)                                  # sum of the given set
T = int(input())                            # Target sum
L_final = []                                # final set which adds up to target sum 'T'
new_L = []                                  # temporary list 

# func(L,T,S) returns a set which may or may not add up to given target;

def func(L,T,S):
    for i in L:
        x = S - i
        if x > T:
            new_L.append(i)
            S = x
        if x < T:
            pass
        if x == T:
            new_L.append(i)
            break
    for i in L:
        if i not in new_L:
            L_final.append(i)
    
    return L_final

# func2() calls func() recursively until the solution is found!

def func2(n=0):
    X = sum(func(L,T,S))
    if X != T:
        new_L.clear()
        L_final.clear()
        L.append(L.pop(n))                  # pop the first element in list and add it to the end of the list
        X = sum(func(L,T,S))
        if X == T:
            print(L_final)
        else:
            func2()
    else:
        print(L_final)

func2()
