'''
Generator Expression: Similar to a list comprehension but uses () instead of []
Creates a generator (iterator) that yields values one at a time
No need to define a function or use yield
Less flexible than a gen func and not reusable

object = (expression for value in iterable), we can apply other styles like in list comprehension to this Gen Expr.
this object can be put under the loop. (it's iterable)
'''

number = int(input("Enter a number to count up to :"))
Counter = (num for num in range(1,number+1))
for n in Counter:
    print(n)

file_name= 'file.txt'
with open(file_name) as file:
    lines = (line.strip() for line in file)
    for line in lines:
        print(line)