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

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve
from Collatz import collatz_eval_help


# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "0 0\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 0)
        self.assertEqual(j, 0)

    def test_read_3(self):
        s = "9999 99999\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 9999)
        self.assertEqual(j, 99999)

    def test_read_4(self):
        s = "123456789 0\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 123456789)
        self.assertEqual(j, 0)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    # -----
    # eval_help
    # -----

    def test_eval_help_1(self):
        n = collatz_eval_help(100)
        self.assertEqual(n, 26)

    def test_eval_help_2(self):
        n = collatz_eval_help(200)
        self.assertEqual(n, 27)

    def test_eval_help_3(self):
        n = collatz_eval_help(300)
        self.assertEqual(n, 17)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 1, 999, 20)
        self.assertEqual(w.getvalue(), "1 999 20\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 1, 999, -1000)
        self.assertEqual(w.getvalue(), "1 999 -1000\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("10 1\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 1 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("5 10\n99 9999\n9999 999999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "5 10 20\n99 9999 262\n9999 999999 525\n")

    def test_solve_3(self):
        r = StringIO("555 5555\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "555 5555 238\n")

    def test_solve_4(self):
        r = StringIO("1 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 1 1\n")

# ----
# main
# ----

if __name__ == "__main__":  # pragma: no cover
    main()

""" # pragma: no cover
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
..................
----------------------------------------------------------------------
Ran 18 tests in 10.015s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          43      0     16      0   100%
TestCollatz.py      79      1      0      0    99%   150
------------------------------------------------------------
TOTAL              122      1     16      0    99%

"""
