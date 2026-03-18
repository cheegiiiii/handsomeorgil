print("Hello world")

with open("data.txt", "r") as file:
    print(file.read())

print("kebab :3")

moni = 0
order = input("what pizza would u like to order S, M or L: ")

if order == "S":
    order1 = print("would you like a extra cheese? Y, N:")
    if order1 == "Y":
        print(f"total is {moni} enjoy! ")
        
else:
    print("bye")


    
import random

list = ["rock", "paper", "scissors"]
a = input("Rock, Paper, Scissors!: ")
b = random.list
user_score = 0
computer_score = 0 
 
while user_score < 3 and computer_score < 0:
    if a == b:
        print("Tie!")
    elif a == "rock" and b == "paper":
        computer_score += 1
        print("computer wins")
    elif a == "scissors" and b == "paper":
        user_score += 1
        print("you win")
    elif a == "rock" and b == "scissors":
        user_score += 1
        print("you win")
    elif a == "scissors" and b == "rock":
        computer_score += 1
        print("computer wins")
    elif a == "paper" and b == "scissors":
        computer_score += 1
        print("computer wins")
    elif a == "paper" and b == "rock":
        user_score += 1
        print("you win")
    else: 
        print("There's something wrong")
        

