turn=0;
res=0;
Questions=["1. What is the Capital city of India?",
"2. what is the SI unit of Force?",
"3. Which is the fastest memory of computer?",
"4. What is the smallest unit of data or info?"]

Options=[["A. Mumbai","B. Delhi","C. Kolkata","D. Chennai"],
["A. Newton","B. Joule","C. Pascal","D. Dyne"],
["A. RAM","B. Cache","C. Register","D. Hard-disk"],
["A. Bit","B. Byte","C. Nibble","D. Word"]];

Answers=["B","A","C","A"];
guesses=[];
print("--------------------Questions--------------------");
for i in Questions:
    print(i);
    for j in Options[turn]:
        print(j)
    guess=input("Enter yrs Answer(A-D):")
    guesses.append(guess)
    if(guess.upper()==Answers[turn]):
        print("Correct Answer!")
        res+=1;
    else:
        print(f"Incorrect Answers!Correct Answer is {Answers[turn]} ")
    turn+=1
    print("----------------------------------------")
    
print("Answers are")
for x in Answers:
    print(x,end=" ")
print("")
print("Guesses are")
for y in guesses:
    print(y.upper(),end=" ")

print("\n-----------RESULT------------")
print(f"Yrs Score out of {len(Questions)} is {res}") 