# Coder une fonction qui permet de calculer n'importe quel terme de la suite de Fibonacci (https://fr.wikipedia.org/wiki/Suite_de_fibonacci)
from math import sqrt

def fibo(n):
    '''renvoie le n-ème terme de la suite de Fibonnacci'''
    a,b = (1+sqrt(5))/2, (1-sqrt(5))/2
    return int((a**n - b**n)/sqrt(5))
    # fib0, fib1 = 0, 1
    # if n == 0:
    #     return fib0
    # if n == 1:
    #     return fib1
    # return fibo(n-2) + fibo(n-1)
    # n1, n2 = 0,1
    # for i in range(2,n):
    #     n1 = n2
    #     n2 = n1+n2
    # return n1
#     n1 = 0
#     n2 = 1
#     print(f'\n le terme numéro {n} de la suite de Fibonacci est : ')
#     for i in range(2, n+1):
#         suivant = n1 + n2
#         #print(suivant,end=', ')
#         n1 = n2
#         n2 = suivant
#     print(n2)
#     return n2    
# #fibo(1000)
    # a=0
    # b=1
    # for i in range(n):
    #     (a,b) = (b,a+b)
    # return a
    
    
#fibo(1000)
    
