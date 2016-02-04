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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_compute

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
        s    = "1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 1)

    def test_read_2 (self) :
        s    = "1 1000000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 1000000)

    def test_read_3 (self) :
        s    = "5 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 5)
        self.assertEqual(j, 1)

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

    # new test_eval start here
    def test_eval_5 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_6 (self) :
        v = collatz_eval(5, 5)
        self.assertEqual(v, 6)
        # 5, 16, 8, 4, 2, 1

    def test_eval_7 (self) :
        v = collatz_eval(10, 10)
        self.assertEqual(v, 7)
        # 10, eval(5)

    def test_eval_8 (self) :
        v = collatz_eval(2, 2)
        self.assertEqual(v, 2)
        # 2, 1

    def test_eval_9 (self) :
        v = collatz_eval(1, 3)
        self.assertEqual(v, 8)
        # 1 -> 1; 2 -> 2; 3-> 3, eval(10) -> 1+7 == 8

    def test_eval_10 (self) :
        v = collatz_eval(999998, 2)
        self.assertEqual(v, 525)
        # 1 -> 1; 2 -> 2; 3-> 3, eval(10) -> 1+7 == 8; 4 -> 3

    def test_eval_11 (self) :
        v = collatz_eval(1, 999999)
        self.assertEqual(v, 525)

    def test_eval_12 (self) :
        v = collatz_eval(900000, 999999)
        self.assertEqual(v, 507)

    def test_eval_13 (self) :
        v = collatz_eval(1234, 5678)
        self.assertEqual(v, 238)

    def test_eval_14 (self) :
        v = collatz_eval(1, 999999)
        self.assertEqual(v, 525)

    def test_eval_15 (self) :
        v = collatz_eval(837799, 837799)
        self.assertEqual(v, 525)

    def test_eval_16 (self) :
        v = collatz_eval(837798, 837798)
        self.assertEqual(v, 132)

    # -------
    # compute
    # -------

    def test_collatz_compute_1 (self) :
        v = collatz_compute(1)
        self.assertEqual(v,1)

    def test_collatz_compute_2 (self) :
        v = collatz_compute(2)
        self.assertEqual(v,2)

    def test_collatz_compute_3 (self) :
        v = collatz_compute(3)
        self.assertEqual(v,8)

    def test_collatz_compute_4 (self) :
        v = collatz_compute(4)
        self.assertEqual(v,3)

    def test_collatz_compute_5 (self) :
        v = collatz_compute(5)
        self.assertEqual(v,6)

    def test_collatz_compute_6 (self) :
        v = collatz_compute(10)
        self.assertEqual(v,7)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 1, 3, 8)
        self.assertEqual(w.getvalue(), "1 3 8\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 9, 0, 9)
        self.assertEqual(w.getvalue(), "9 0 9\n")


    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n")

    def test_solve_2 (self) :
        r = StringIO("1 1\n1 2\n1 3\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n1 2 2\n1 3 8\n")

    def test_solve_3 (self) :
        r = StringIO("1 1\n1 2\n1 3\n1 4\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n1 2 2\n1 3 8\n1 4 8\n")


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
