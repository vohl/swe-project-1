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
        s    = "  13    100\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  13)
        self.assertEqual(j, 100)

    def test_read_2 (self) :
        s    = "99    11     \n"
        i, j = collatz_read(s)
        self.assertEqual(i,  99)
        self.assertEqual(j,  11)

    def test_read_3 (self) :
        s    = "    1   404   \n  "
        i, j = collatz_read(s)
        self.assertEqual(i,   1)
        self.assertEqual(j, 404)


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
        v = collatz_eval(8, 9)
        self.assertEqual(v, 20)

    def test_eval_6 (self) :
        v = collatz_eval(900, 900)
        self.assertEqual(v, 55)

    def test_eval_7 (self) :
        v = collatz_eval(101, 11)
        self.assertEqual(v, 119)

    def test_eval_8 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_9 (self) :
        v = collatz_eval(11, 1990)
        self.assertEqual(v, 182)

    def test_eval_10 (self) :
        v = collatz_eval(1, 109)
        self.assertEqual(v, 119)

    def test_eval_11 (self) :
        v = collatz_eval(10, 1000)
        self.assertEqual(v, 179)

    def test_eval_12 (self) :
        v = collatz_eval(999, 99999)
        self.assertEqual(v, 351)

    def test_eval_13 (self) :
        v = collatz_eval(649222, 755895)
        self.assertEqual(v, 504)

    def test_eval_14 (self) :
        v = collatz_eval(118128, 116353)
        self.assertEqual(v, 305)

    def test_eval_15 (self) :
        v = collatz_eval(105192, 103214)
        self.assertEqual(v, 341)

    def test_eval_16 (self) :
        v = collatz_eval(999999, 999999)
        self.assertEqual(v, 259)       

    def test_eval_17 (self) :
        v = collatz_eval(651312, 639479)
        self.assertEqual(v, 416)

    def test_eval_18 (self) :
        v = collatz_eval(649222, 755895)
        self.assertEqual(v, 504)

    def test_eval_19 (self) :
        v = collatz_eval(784731, 15401)
        self.assertEqual(v, 509)

    def test_eval_20 (self) :
        v = collatz_eval(414512, 62211)
        self.assertEqual(v, 449)

    def test_eval_21 (self) :
        v = collatz_eval(753003, 994495)
        self.assertEqual(v, 525)

    def test_eval_22 (self) :
        v = collatz_eval(489811, 956669)
        self.assertEqual(v, 525)


    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 0, 0, 0)
        self.assertEqual(w.getvalue(), "0 0 0\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 1, 2, 3)
        self.assertEqual(w.getvalue(), "1 2 3\n")
    
    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 10, 2, 11)
        self.assertEqual(w.getvalue(), "10 2 11\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1 (self) :
        r = StringIO("8 8\n8 9\n9 100\n111 999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "8 8 4\n8 9 20\n9 100 119\n111 999 179\n")

    def test_solve_2 (self) :
        r = StringIO("4 5\n50 200\n101 11\n500 404\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "4 5 6\n50 200 125\n101 11 119\n500 404 142\n")

    def test_solve_3 (self) :
        r = StringIO("90 99\n403 430\n98 89\n12 120\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "90 99 119\n403 430 134\n98 89 119\n12 120 119\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

""" #pragma: no cover
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
