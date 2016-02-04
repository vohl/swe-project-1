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

    def test_read_1 (self) :
        s    = "7 7\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 7)
        self.assertEqual(j, 7)

    def test_read_2 (self) :
        s    = "8 -1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 8)
        self.assertEqual(j, -1)

    def test_read_3 (self) :
        s    = "1 999999\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
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

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, -1, -2, 1000000)
        self.assertEqual(w.getvalue(), "-1 -2 1000000\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 0, 999999, 15000000)
        self.assertEqual(w.getvalue(), "0 999999 15000000\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, "hello", "world", "UTCS")
        self.assertEqual(w.getvalue(), "hello world UTCS\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1 (self) :
        r = StringIO("1 1\n10 10\n1 15\n1000 2000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n10 10 7\n1 15 20\n1000 2000 182\n")

    def test_solve_2 (self) :
        r = StringIO("10 1\n 200 100\n 210 201\n1000 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve_3 (self) :
        r = StringIO("1 3\n999998 999999\n999997 999999\n 999999 999999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 3 8\n999998 999999 259\n999997 999999 259\n999999 999999 259\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
................
----------------------------------------------------------------------
Ran 16 tests in 0.064s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          44      0     20      0   100%   
TestCollatz.py      75      1      2      1    97%   132, 129->132
------------------------------------------------------------
TOTAL              119      1     22      1    99%   
"""