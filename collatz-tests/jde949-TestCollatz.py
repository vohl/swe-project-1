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

from Collatz import collatz_read, collatz_eval, collatz_num, collatz_print, collatz_solve

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
        s    = "100 50\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j,  50)

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
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_6 (self) :
        v = collatz_eval(210, 100)
        self.assertEqual(v, 125)

    def test_eval_7 (self) :
        v = collatz_eval(47, 342)
        self.assertEqual(v, 144)

    # ---
    # num
    # ---

    def test_num_1 (self) :
        v = collatz_num(1)
        self.assertEqual(v, 1)

    def test_num_2 (self) :
        v = collatz_num(10)
        self.assertEqual(v, 7)

    def test_num_3 (self) :
        v = collatz_num(32)
        self.assertEqual(v, 6)

    # ---
    # num_eval
    # ---

    def test_num_eval_1 (self) :
        v = collatz_num(999999)
        e = collatz_eval(999999,999999)
        self.assertEqual(e, v)

    def test_num_eval_2 (self) :
        v1 = collatz_num(249)
        v2 = collatz_num(250)
        v3 = collatz_num(251)

        e = collatz_eval(249,251)
        self.assertEqual(e, max(v1,max(v2,v3)))

    def test_num_eval_3 (self) :
        v1 = collatz_num(499)
        v2 = collatz_num(500)

        e = collatz_eval(499,500)
        self.assertEqual(e, max(v1,v2))

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertEqual(w.getvalue(), "10 1 20\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("10 1\n100 200\n201 210\n1000 900\n108424 773937\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 1 20\n100 200 125\n201 210 89\n1000 900 174\n108424 773937 509\n")



# ----
# main
# ----

if __name__ == "__main__" :
    main()
    