cou = 0
print("What's the capital city of Nepal ? ")
a = input("Enter the answer = ")
print("How many continents in the World? ")
b = int(input("Enter the answer = "))
print("Who's the Richest person in the world ? ")
c = input("Enter the answer = ")
print("Who's the Father of computer ? ")
d = input("Enter the answer = ")
print("Which's the Highest peak in the world?")
e = input("Enter the answer =")

dictn = {a: "ktm", b: 7, c: "elon musk", d: "charles babbage", e: "mt everest"}
for i, j in dictn.items():
  if (i == j):
    cou += 1
    print("Right answer.")

  else:
    print("Wrong answer.", "Right Answer = ", j)

print("Right Answers = ", cou)
print(f"Congratulations u have scored {cou} out of {len(dictn)}")