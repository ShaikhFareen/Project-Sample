import random
def guessing_game():
  number = random.randint(0,10)
  for i in range(0,3):  
    user = int(input("guess the number"))
    if user == number:
        print("Hurray!!")
        print(f"you guessed the number right it's {number}")
        break 
    elif user > number:
        print(f"{user} is too high")
    elif user < number:
        print(f"{user} is too low")
  else:
    print(f"Better luck next time and the correct number is {number} ")
guessing_game()