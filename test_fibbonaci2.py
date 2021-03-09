
import unittest

from fibbonaci import recur_fibo

def recur_fibo(x):
    if x <= 1:
       return x
    else:
       return(recur_fibo(x-1) + recur_fibo(x-2))


def test_fibbonaci():
    assert recur_fibo(9) == 34




