#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # test two of the same number as input
    def test_read_2 (self) :
        s = "99 99\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 99)
        self.assertEqual(j, 99)

    # test the case where the input numbers are flipped
    def test_read_3 (self) :
        s = "10 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j, 1)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        # largest cycle length should be 20
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        # largest cycle length should be 125
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        # largest cycle length should be 89
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        # largest cycle length should be 174
        self.assertEqual(v, 174)

    # flip the input from test_eval_4... the output should be the same
    def test_eval_5 (self) :
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174)

    # test the case where the two input numbers are the same
    def test_eval_6 (self) :
        v = collatz_eval(10, 10)
        self.assertEqual(v, 7)

    # 2 numbers with only 1 possible solution
    def test_eval_7 (self) :
        v = collatz_eval(20, 21)
        self.assertEqual(v, 8)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # weird case where the inputs and output is the same
    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    # input should stay in the same form
    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertEqual(w.getvalue(), "10 1 20\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        # fixed
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # added test
    def test_solve_2 (self) :
        r = StringIO("1000 900\n210 201\n200 100\n10 1\n")
        w = StringIO()
        collatz_solve(r, w)
        # fixed
        self.assertEqual(w.getvalue(), "1000 900 174\n210 201 89\n200 100 125\n10 1 20\n")

    # added test
    def test_solve_3 (self) :
        r = StringIO("999998 999997\n956354 956358\n354 363\n")
        w = StringIO()
        collatz_solve(r, w)
        # fixed
        self.assertEqual(w.getvalue(), "999998 999997 259\n956354 956358 78\n354 363 51\n")



# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
