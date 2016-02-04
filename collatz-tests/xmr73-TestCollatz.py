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
        s = "100 200\n";
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j, 200)

    def test_read_3 (self) :
        s = "10 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j, 1) 

    def test_read_4 (self) :
        s = "1000000 2000000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1000000)
        self.assertEqual(j, 2000000) 

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

    def test_eval_5(self) :
        v = collatz_eval(687023, 680304)
        self.assertEqual(v, 398)

    def test_eval_6(self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_7(self) :
        v = collatz_eval(689640, 691867)
        self.assertEqual(v, 336)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_4 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("680304 687023\n669922 674486\n747292 747507\n861524 862840\n419840 420010\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "680304 687023 398\n669922 674486 367\n747292 747507 349\n861524 862840 326\n419840 420010 281\n")

    def test_solve_3 (self) :
        r = StringIO("844648 845864\n919520 920496\n901120 905569\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "844648 845864 401\n919520 920496 432\n901120 905569 401\n")

    def test_solve_4 (self) :
        r = StringIO("999999 999999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "999999 999999 259\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
% coverage3 run --branch xmr73-TestCollatz.py >  xmr73-TestCollatz.out 2>&1



% coverage3 report -m                   >> xmr73-TestCollatz.out



% cat TestCollatz.out

...................
----------------------------------------------------------------------
Ran 19 tests in 4.287s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          39      0     20      3    95%   44->66, 60->48, 94->93
TestCollatz.py      84      1      2      1    98%   144, 141->144
------------------------------------------------------------
TOTAL              123      1     22      4    97%   
"""
