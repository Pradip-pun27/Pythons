try:
    print("Error handling")
    print(int("ramesh")) #This is a ValueError
    print(1+"ram") # This is a TypeError
except ValueError:
    print("Error1")  
except TypeError:
    print("Error2")

else:
    print("All Fine")