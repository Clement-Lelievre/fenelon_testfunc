# from func import f, g
# import pytest
# from random import randint

# # testing f
# def test_argument_positif():
#     for i in range(0,10**6):
#         assert f(i) == 3*i
        
# def test_argument_negatif():
#     for i in range(-10**6,0):
#         assert f(i) == 0

# # testing g
# long_number = str(randint(10**25,10**40))
# long_number += ('1' + long_number[::-1])

# @pytest.mark.parametrize("mot, is_palindrome",[('kayak',True),('ab',False),('121',True),('appa',True),('azerty0ytreza',True),(long_number,True)])
# def test_palindrome_bonnereponse(mot, is_palindrome):
#     assert g(mot) is is_palindrome 
  
# def test_palindrome_bontype():
#     for i in range(-10**6,10**6):
#         assert isinstance(g(i), bool)
   
