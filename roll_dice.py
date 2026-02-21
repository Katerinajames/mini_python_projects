
import random
times=7  #  The times we want our dices to roll
n=0   #Our counter
def roll_dice():  #Method
	d1=random.randint(1,7)
	d2=random.randint(1,7)
	return d1,d2
print("----------------------------")
print("Welcome to the Dice Rolling Simulator!")
while n<7:
 user_input=input("Press Enter to roll the dice or q  to quit\n" ) 
 if user_input=="q":
     print("Thanks for playing")
     break
 elif user_input == '':
	  d1, d2=roll_dice()
	  print(f"The result of the {n} roll is {d1} {d2}")
	  n=n+1
 else:
	 print("Invalid input")
print(f"The total number of the rolls is {n}")
 
