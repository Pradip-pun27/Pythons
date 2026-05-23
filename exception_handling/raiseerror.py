
a=int(input("Enter 1st number ="))
b=int(input("Enter 2nd number ="))
if b==0:
    raise ValueError("Denominator can't be zero") # By this we crashed ours program on our own and prevent it from executing unnecessary line of codes.
print(a/b)

