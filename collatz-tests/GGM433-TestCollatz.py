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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, range_max_cycle

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
        s    = "10 2\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j, 2)

    def test_read_2 (self) :
        s    = "847847 26819\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 847847)
        self.assertEqual(j, 26819)

    def test_read_3 (self) :
        s    = "1000 9299\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1000)
        self.assertEqual(j, 9299)

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

    def test_eval_5 (self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_6 (self):
        v = collatz_eval(9, 9)
        self.assertEqual(v, 20)

    def test_eval_8 (self):
        v = collatz_eval(543543, 432440)
        self.assertEqual(v, 470)

    def test_eval_9 (self) :
        v = collatz_eval(999999, 999999)
        self.assertEqual(259, v)

    def test_eval_10 (self) :
        v = collatz_eval(999999, 1)
        self.assertEqual(v, 525)

    def test_eval_11 (self) :
        v = collatz_eval(70424, 27816)
        self.assertEqual(v, 340)


    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")


    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 0, 17, 934)
        self.assertEqual(w.getvalue(), "0 17 934\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, -7, 8376, 21000000)
        self.assertEqual(w.getvalue(), "-7 8376 21000000\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, "A", "b", "C")
        self.assertEqual(w.getvalue(), "A b C\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")


    def test_solve_1 (self) :
        r = StringIO("1 1\n5 6688\n6800 63\n800 5250\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n5 6688 262\n6800 63 262\n800 5250 238\n")

    def test_solve_2 (self) :
        r = StringIO("53408 811977\n210 201 200 100\n424701 273437\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "53408 811977 509\n210 201 89\n424701 273437 449\n")

    def test_solve_3 (self) :
        r = StringIO("10 1\n999999 999999\n100 200\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 1 20\n999999 999999 259\n100 200 125\n")

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
