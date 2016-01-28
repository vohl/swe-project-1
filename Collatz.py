#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

cache = [None]*1000001

#------------
#cycle_length
#------------
def cycle_length (n) :
    """
    n is positive integer
    return the calculated cycle length for n
    """
    assert n > 0
    if cache[n] != None :
        return cache[n]
    m = n
    count = 1
    while m > 1 :
        if cache[m] != None :
            cache[n] = cache[m] + count - 1
            return cache[m] + count - 1
        if (m % 2) == 0 :
            m = (m // 2)
            count += 1
        else :
            m = m + (m // 2) + 1
            count += 2
    assert count > 0
    cache[n] = count
    return count

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    assert s != None
    a = s.split()
    assert a[0] != None
    assert a[1] != None
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert i > 0
    assert j > 0
    rangeMin = 0
    rangeMax = 0
    #Used to cut out values under half the max range
    possibleMin = 0

    #grabing the min and max of the input
    if i < j :
        rangeMin = i
        rangeMax = j
    elif j < i :
        rangeMax = i
        rangeMin = j
    else :
        return cycle_length(i)

    assert rangeMin > 0
    assert rangeMax > 0
    possibleMin = rangeMax // 2 + 1
    if possibleMin > rangeMin :
        rangeMin = possibleMin

    max = 0

    #calculating the cycle length while tracking the max
    while rangeMin < rangeMax :
        cl = cycle_length(rangeMin)
        if cl > max :
            max = cl
        rangeMin += 1

    assert max > 0
    return max

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    assert i != None
    assert j != None
    assert v != None
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    #Should I use asserts for this or nah
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
