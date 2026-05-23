'''
Iterator: An object that returns elements one at a time from a sequence (or data stream  :file)
and remember its position between calls.

A Py object is an iterator if it has:
__iter__() -> Returns the iterator object itself
__next__() -> Returns the next item in the sequence (raises StopIteration when no more items)
'''
import random

class Dice:
    def __init__(self, rolls):
        self.rolls = rolls
        self.count = 0

    def __iter__(self):
         return self

    def __next__(self):
        if self.count < self.rolls:
            self.count+=1
            return random.randint(1,6)
        else:
            raise StopIteration

dice = [die for die in Dice(7)]
print(dice)


#Under the hood below codes get executed

# dice = Dice(3)
# iterator = iter(dice) or dice.__iter__()
# while True:
#     try:
#         roll = next(iterator)
#         print(roll)
#     except StopIteration:
#         break
