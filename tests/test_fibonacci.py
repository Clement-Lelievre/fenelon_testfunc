import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fibonacci import fibo
import pytest
from math import sqrt

def fib_recursive(n):  # this recursive definition is very slow as the same values are recalculated many times
    fib0, fib1 = 0, 1
    if n == 0:
        return fib0
    if n == 1:
        return fib1
    return fib(n-2) + fib(n-1)

def fib_exact(n):
    a,b = (1+sqrt(5))/2, (1-sqrt(5))/2
    return int((a**n - b**n)/sqrt(5))

# testing the fibo function

def test_fibo_value():
    for i in range(0,10**1):
        assert fibo(i) == fib_exact(i)
        
def test_fibo_type():
    for i in range(0,10**1):
        assert isinstance(fibo(i), int)