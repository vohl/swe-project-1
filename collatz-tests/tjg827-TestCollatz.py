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

    def test_read (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # My tests

    def test_read_a1 (self) :
        s    = "199 42 4422\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 199)
        self.assertEqual(j, 42)

    def test_read_a2 (self) :
        s    = " 5 4\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 5)
        self.assertEqual(j, 4)

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

    # My tests

    def test_eval_a1 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_a2 (self) :
        v = collatz_eval(1, 2)
        self.assertEqual(v, 2)

    def test_eval_a3 (self) :
        v = collatz_eval(1, 10000)
        self.assertEqual(v, 262)

    def test_eval_a4 (self) :
        v = collatz_eval(4, 1)
        self.assertEqual(v, 8)

    def test_eval_a5 (self) :
        v = collatz_eval(3, 3)
        self.assertEqual(v, 8)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # My tests

    def test_print_a1 (self) :
        w = StringIO()
        collatz_print(w, 4, 1, 8)
        self.assertEqual(w.getvalue(), "4 1 8\n")

    def test_print_a2 (self) :
        w = StringIO()
        collatz_print(w, 101, 110, 114)
        self.assertEqual(w.getvalue(), "101 110 114\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # My tests

    def test_solve_a1 (self) :
        r = StringIO(" 1   1\n1    2\n 1    10000")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n1 2 2\n1 10000 262\n")

    def test_solve_a2 (self) :
        r = StringIO("4 1\n3 3")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "4 1 8\n3 3 8\n")

# ----
# main
# ----

if __name__ == "__main__" : # pragma: no cover
    main()

""" # pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
..................
----------------------------------------------------------------------
Ran 18 tests in 0.794s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          37      0     16      0   100%
TestCollatz.py      73      0      0      0   100%
------------------------------------------------------------
TOTAL              110      0     16      0   100%   
"""
