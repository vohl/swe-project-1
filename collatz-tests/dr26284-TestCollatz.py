#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2015
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
    def test_read_2 (self) :
        s = "0 900\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 0)
        self.assertEqual(j, 900)
    def test_read_3 (self) :
        s = "3 3\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 3)
        self.assertEqual(j, 3)
    def test_read_4 (self) :
        s = "900 901\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 900)
        self.assertEqual(j, 901)

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
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 89, 34, 2)
        self.assertEqual(w.getvalue(), "89 34 2\n")
    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 0, 0, 0)
        self.assertEqual(w.getvalue(), "0 0 0\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    def test_solve_2 (self) :
        r = StringIO("1 1\n8 40\n55 56\n33 33\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n8 40 112\n55 56 113\n33 33 27\n")
    def test_solve_3 (self) :
        r = StringIO("40 46\n3 509\n25 26\n127 189\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "40 46 110\n3 509 144\n25 26 24\n127 189 125\n")
    def test_solve_4 (self) :
        r = StringIO("46 40\n509 3\n687 46\n68 2\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "46 40 110\n509 3 144\n687 46 145\n68 2 113\n")

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
