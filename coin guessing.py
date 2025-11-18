import random
my_random=input("""Welcom to the coin guessing game!
Choose a method to toss the coin
1.Using random.random()
2.Using random.randint()""")

if my_random=='1':
    x=random.random()
    if x<0.5:
        result="heads"
    else:
        result="tails"
        
elif my_random=="2":
    x=random.randint(0,1)
    
    if x==0:
         result="Heads"
    else:
         result="Tails"
else:
    print("Invalid choice. Please select either 1 or 2.")
user_guess=input("Make your guess! Type 'Heads' or 'Tails': ").lower()

if user_guess != "heads" and user_guess !="tails":
    print("Invalid choice! Please choose either 'Heads' or 'Tails'.")

if user_guess==result:
    print("congratulations! You won!")
else:
    print(f"Sorry, you lost! The correct answer was {result}.")