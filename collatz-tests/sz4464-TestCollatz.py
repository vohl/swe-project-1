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

    def test_read_0 (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_1 (self) :
        s    = "1       10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2 (self) :
        s    = "1000 1111\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1000)
        self.assertEqual(j, 1111)

    def test_read_3 (self) :
        s    = "1000000 999999\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1000000)
        self.assertEqual(j, 999999)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5 (self) :
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174)

    def test_eval_6 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_7 (self) :
        v = collatz_eval(9, 9)
        self.assertEqual(v, 20)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 900, 1000, 1)
        self.assertEqual(w.getvalue(), "900 1000 1\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, "1000", "foo", "18 37")
        self.assertEqual(w.getvalue(), "1000 foo 18 37\n")

    def test_print_4 (self) :
        w = StringIO()
        collatz_print(w, -1, -2, -21)
        self.assertEqual(w.getvalue(), "-1 -2 -21\n")   

    # -----
    # solve
    # -----

    def test_solve_0 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1 (self) :
        r = StringIO("1 5\n6 10\n11 15\n16 20\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 5 8\n6 10 20\n11 15 18\n16 20 21\n")


    def test_solve_2 (self) :
        r = StringIO("1 1000\n1000 1\n1000 2000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1000 179\n1000 1 179\n1000 2000 182\n")

    def test_solve_3 (self) :
        r = StringIO("1 1\n1 2\n1 3\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n1 2 2\n1 3 8\n")

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
