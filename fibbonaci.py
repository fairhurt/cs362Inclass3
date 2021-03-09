
import unittest


import fibbonaci
def recur_fibo(x):
    if x <= 1:
       return x
    else:
       return(recur_fibo(x-1) + recur_fibo(x-2))



