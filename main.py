# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
'''
#############################################
# All tasks should be solved using recursion
#############################################
Task 1

from typing import Optional
def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
    """
    Returns  x ^ exp

    >>> to_power(2, 3) == 8
    True

    >>> to_power(3.5, 2) == 12.25
    True

    >>> to_power(2, -1)
    ValueError: This function works only with exp > 0.
    """
    pass


Task 2

from typing import Optional
def is_palindrome(looking_str: str, index: int = 0) -> bool:
    """
    Checks if input string is Palindrome
    >>> is_palindrome('mom')
    True

    >>> is_palindrome('sassas')
    True

    >>> is_palindrome('o')
    True
    """
    pass


Task 3

from typing import Optional
def mult(a: int, n: int) -> int:
    """
    This function works only with positive integers

    >>> mult(2, 4) == 8
    True

    >>> mult(2, 0) == 0
    True

    >>> mult(2, -4)
    ValueError("This function works only with postive integers")
    """
Task 4

def reverse(input_str: str) -> str:
    """
    Function returns reversed input string
    >>> reverse("hello") == "olleh"
    True
    >>> reverse("o") == "o"
    True
    """
Task 5

def sum_of_digits(digit_string: str) -> int:
    """
    >>> sum_of_digits('26') == 8
    True

    >>> sum_of_digits('test')
    ValueError("input string must be digit string")
'''
def to_power(x, exp) :
    if exp<0 or int(exp)!=exp:
        raise ValueError
    if exp==0:
        return 1
    return to_power(x,exp-1)*x

def is_palindrome(str) -> bool:
    if str[0]!=str[-1]:
        return False
    if len(str)<3:
        return True
    return is_palindrome(str[1:-1])
def mult(a, n) -> int:
    if a<0 or n<0:
        raise ValueError
    if n==0:
        return 0
    return mult(a,n-1)+a
def sum_of_digits(digit: str):
    if digit=='':
        return 0
    if not digit.isdigit():
        raise ValueError
    return int(digit[0])+sum_of_digits(digit[1:])



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(to_power(2,3))
    print(to_power(3.5, 2))
    str='murmay'
    print(is_palindrome('mom'))
    print(is_palindrome('sassas'))
    print(is_palindrome('sakksas'))
    print(mult(2, 4))
    print(mult(2, 0) == 0)
    print(sum_of_digits('26'))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
