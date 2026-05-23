foods=[]
prices=[]
total=0
while True:
    food=input("Enter the name of food u wanna buy(Enter q for quit) = ")
    if food.lower()=="q":
        break;
    else:
        foods.append(food)
        price=float(input("Enter the Price of this food =$"))
        prices.append(price)

print("The list of the Foods u entered are =",foods)
print("Their respective prices =",prices)
print("The items in the list are ")
for i in foods:
    print(f"{i}",end=" ")
print(" ")
for j in prices:
    total+=j
print(f"{total} needs to pay.")

