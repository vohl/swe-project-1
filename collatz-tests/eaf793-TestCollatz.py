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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_recurse, collatz_tile

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

    # -------
    # recurse
    # -------

    def test_recurse_1(self):
        v = collatz_recurse(5, 1)
        self.assertEqual(v, 6)

    def test_recurse_2(self):
        v = collatz_recurse(9, 1)
        self.assertEqual(v, 20)

    def test_recurse_3(self):
        v = collatz_recurse(999999, 1)
        self.assertEqual(v, 259)

    # ----
    # tile
    # ----

    def test_tile_1(self):
        v = collatz_tile(201)
        self.assertEqual(v, 128)

    def test_tile_2(self):
        v = collatz_tile(1)
        self.assertEqual(v, 122)

    def test_tile_3(self):
        v = collatz_tile(999600)
        self.assertEqual(v, 290)

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

    def test_eval5 (self) :
        v = collatz_eval(200, 100)
        self.assertEqual(v, 125)

    def test_eval6 (self) :
        v = collatz_eval(13, 1)
        self.assertEqual(v, 20)

    def test_eval7 (self) :
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2 (self) :
        r = StringIO("200 100\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "200 100 125\n")

    def test_solve3 (self) :
        r = StringIO("14 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "14 1 20\n")

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
