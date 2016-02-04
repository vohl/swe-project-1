#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# K.C. Hawes-Domingue
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

    # Tests reading normal input
    def test_read_1 (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # Tests reading input with extra whitespace
    def test_read_2 (self) :
        s = " 1    10   \n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    # ----
    # eval
    # ----

    # Max cycle length of [1, 10] is 20
    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    # Max cycle length of [100, 200] is 125
    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    # Max cycle length of [201, 210] is 89
    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    # Max cycle length of [900, 1000] is 174
    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    # Max cycle length of [1, 1] is 1
    def test_eval_5 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    # Max cycle length of [555, 555] is 31
    def test_eval_6 (self) :
        v = collatz_eval(555, 555)
        self.assertEqual(v, 31)

    # Max cycle length of [200, 100] is 125
    def test_eval_7 (self) :
        v = collatz_eval(200, 100)
        self.assertEqual(v, 125)

    # -----
    # print
    # -----

    # Tests printing expected values
    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # Tests printing unexpected values
    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, -1, 0, 12345678)
        self.assertEqual(w.getvalue(), "-1 0 12345678\n")

    # Tests printing subsequent values
    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 0, 1, 2)
        self.assertEqual(w.getvalue(), "0 1 2\n")

    # -----
    # solve
    # -----

    # Tests solving expected input
    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # Tests solving a case of j < i
    def test_solve_2 (self) :
        r = StringIO("200 100\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "200 100 125\n")
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
Ran 7 tests in 0.000s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          12      0      2      0   100%
TestCollatz      33      1      2      1    94%   81
---------------------------------------------------------
TOTAL            45      1      4      1    96%
"""
