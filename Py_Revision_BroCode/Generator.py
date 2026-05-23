'''
Generator: Function that behaves like an iterator. (it can be used in a for loop)
Pauses a function, returns a value, then resumes.
Uses 'yield' keyword instead of 'return'.
Iterate without loading everthing into memory (eg. reading large files)
return = Pouring bucket
yield = drip faucet
'''

def count_to(n):
    count =1
    while count <= n:
        yield count # when yield keyword encountered it'll pause, return current value and resumes later when f gets called.
        count+=1

number = int(input("Enter a number to count to:"))
for n in count_to(number):
    print(n)

# Under the hood it seems like this:
# ans = count_to(number)
# while True:
#     try:
#         print(next(ans))
#     except StopIteration:
#         break


def read_file(file_name):
    with open(file_name) as file:
        for line in file:
            yield line.strip()

file_name = 'file.txt'
for line in read_file(file_name):
    print(line)
