# CS2021 Lab 02 - Required Questions
## Modify this file by adding your salutation and code. 
## Once you pass all the doctests, then 
## you can then submit you program for credit. 

_author_ = "Eli Pappas"
_credits_ = ["No Helpers"]
_email_ = "pappaseh@mail.uc.edu" # Your email address

#  RQ1
"""
Write a function day_name that converts an integer number 0 to 6 into the name of a day. Assume day 0 is “Sunday”. Your function should return error message if the arguments to the function are not valid. 
"""
def day_name(n):
    """
    >>> day_name(3) 
    'Wednesday'
    >>> day_name(6) 
    'Saturday'
    >>> day_name(42)
    'Invalid argument'
    """
    "*** YOUR CODE HERE ***"
    
    if(n == 0):
        print('\'Sunday\'')
    elif(n == 1):
        print('\'Monday\'')
    elif(n == 2):
        print('\'Tuesday\'')
    elif(n == 3):
        print('\'Wednesday\'')
    elif(n == 4):
        print('\'Thursday\'')
    elif(n == 5):
        print('\'Friday\'')
    elif(n == 6):
        print('\'Saturday\'')
    else:
        print('\'Invalid argument\'')
    

#  RQ2
def two_of_three(a, b, c):
    """Return value using only a one-line return statement.  The value should be the
    sum of two squares x*x + y*y, where x and y are the two largest members of the set of
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return max(a,b)**2 + max(b,c)**2


#  RQ3
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    """
    "*** YOUR CODE HERE ***"
    fac = []
    for x in range(1, n):
        if n % x == 0:
            fac.append(x)  # if x is divisible by n append to factor list
    print(fac[-1])


         
#  RQ4
def keeper(pred, n):
    """Print the numbers between 1 and n which satisfy the predicate pred.

    >>> keeper(lambda x: x%2 == 0, 15)
    2 4 6 8 10 12 14 
    >>> keeper(lambda x: x%7 == 0, 40)
    7 14 21 28 35 
    """
    "*** YOUR CODE HERE ***"  
    data = []
    for x in range(1,n):
        data.append(x)
    a = filter(pred,data)
    b = list(a)
    [print(i, end=' ') for i in b]

    
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)