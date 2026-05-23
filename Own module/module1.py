def fact(n):
    '''
    This Function is
    to show the nth fibonacci term.
    '''
    if(n==1 or n==0):
        return n
    else:
        return fact(n-1)+fact(n-2)


if __name__ =="__main__":
    print(fact.__doc__)#Docstring of python
    num=int(input("Enter any number ="))
    print(f"The nth fibo number is {fact(num)}");

# print(__name__)=> It will give __main__ if program run from original file otherwise will show module1 as o/p
