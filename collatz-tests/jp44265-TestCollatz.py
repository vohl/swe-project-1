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

from Collatz import collatz_read, collatz_eval, find_cycle_len, collatz_print, collatz_solve

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
        s = "117 343\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 117)
        self.assertEqual(j, 343)

    def test_read_3 (self) :
        s = "12 34\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 12)
        self.assertEqual(j, 34)

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
        v = collatz_eval(9000, 10000)
        self.assertEqual(v, 260)

    def test_eval_6(self) :
        v = collatz_eval(11000, 10000)
        self.assertEqual(v, 268)

    # -----------------
    # find cycle length
    # -----------------

    def test_find_cycle_len_1 (self) :
        m = find_cycle_len(117)
        self.assertEqual(m, 21)

    def test_find_cycle_len_2 (self) :
        m = find_cycle_len(343)
        self.assertEqual(m, 126)

    def test_find_cycle_len_3 (self) :
        m = find_cycle_len(104)
        self.assertEqual(m, 13)

    def test_find_cycle_len_4 (self) :
        m = find_cycle_len(1)
        self.assertEqual(m, 1)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 1, 11, 20)
        self.assertEqual(w.getvalue(), "1 11 20\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 117, 343, 144)
        self.assertEqual(w.getvalue(), "117 343 144\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("50 100\n75 117\n9000 10000\n10000 11000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "50 100 119\n75 117 119\n9000 10000 260\n10000 11000 268\n")

    def test_solve_3 (self) :
        r = StringIO("1 1\n117 117\n1001 1001\n2 2\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n117 117 21\n1001 1001 143\n2 2 2\n")

    def test_solve_4 (self) :
        r = StringIO("145 147\n880 885\n898 899\n927 927\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "145 147 117\n880 885 117\n898 899 117\n927 927 117\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

""" #pragma: no cover
coverage3 run    --branch TestCollatz.py >  TestCollatz.tmp 2>&1
coverage3 report -m                      >> TestCollatz.tmp
cat TestCollatz.tmp
....................
----------------------------------------------------------------------
Ran 20 tests in 0.159s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          47      0     24      1    99%   98->-73
TestCollatz.py      83      0      0      0   100%   
------------------------------------------------------------
TOTAL              130      0     24      1    99%   
"""
