#Simple calculator for arithmetic operators in python between 2 numbers.
num1= int(input("Enter number1 = "))
num2= int(input("Enter number2 = "))
ans = int(input("Enter number in between 1-8 = "))
while(num2!=0):
  if(ans ==1):
    print(f"The sum of {num1} and {num2} = {num1 + num2}")
    break
  elif(ans ==2):
   print(f"The difference of {num1} and {num2} = {abs(num1-num2)}")
   break
  elif(ans ==3):
   print(f"The Multiplication of {num1} and {num2} = {num1 * num2}")
   break
  elif(ans ==4):
   print(f"The Division of {num1} by {num2} = {num1 / num2}")
   break
  elif(ans ==5):
   print(f"The Remainder comes after division of  {num1} by {num2} = {num1 % num2}")
   break
  elif(ans==6):
    print(f"The answer after raising {num1} into the power of {num2} = {pow(num2,num1)}")
  elif(ans==7):
    if(num1>num2):
      print(f"{num1} is greater than {num2}")
    else:
      print(f"{num2} is greater than {num1}")
    break
  elif(ans==8):
    a= lambda x,y : pow(x,y)
    print(f"The answer after raising {num2} into the power of {num1} = ",a(num1,num2))
    break
  else:
    print('Invalid input given')
    break
  




  