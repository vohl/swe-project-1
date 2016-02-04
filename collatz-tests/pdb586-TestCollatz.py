#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Paul Bass
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
        s    = "11124 111\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  11124)
        self.assertEqual(j, 111)

    def test_read_2 (self) :
        s    = "99 999999\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  99)
        self.assertEqual(j, 999999)

    def test_read_3 (self) :
        s    = "15 20 20\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  15)
        self.assertEqual(j, 20)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_2fail (self) :
        v = collatz_eval(100, 200)
        self.assertNotEqual(v, 1)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_3fail (self) :
        v = collatz_eval(201, 210)
        self.assertNotEqual(v, 55)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_4fail (self) :
        v = collatz_eval(900, 1000)
        self.assertNotEqual(v, 500)

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
        collatz_print(w, 100, 1000, 500)
        self.assertEqual(w.getvalue(), "100 1000 500\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 1, 1000000000, 20)
        self.assertEqual(w.getvalue(), "1 1000000000 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve1 (self) :
        r = StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve2 (self) :
        r = StringIO("1 1\n100 100\n123456 654321\n999999 999999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n100 100 26\n123456 654321 509\n999999 999999 259\n")

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
