while True:
    try:
        a=int(input("Enter the num1 ="))
        b=int(input("Enter the num2 ="))
        print(f"The Quotient is {a/b}")

    except ValueError as e1:
        print("Type error")
    except ZeroDivisionError as e2:
       print("Denominator can't be zero in math.")

    else:
        print("Try block is fine.")

    finally:
        print("This will executed alz depsite of except block executed or not.")
        break

