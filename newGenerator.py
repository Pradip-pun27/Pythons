def Number_Gen(n):
    for num in range(1,n):
        yield num

value=Number_Gen(4)   
print(next(value))
print(next(value))
print(next(value))


def Generator():
    for i in range(100000):
        yield i
    
result=Generator()
print(next(result))
# for i in result:
#     print(i,end="")
