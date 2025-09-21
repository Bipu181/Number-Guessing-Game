
def guessing_game():
    import random
    print("Welcome To Number Guessing Game 🎮")
    random_number=random.randint(1,20)
    user_name=input("What is your name?\n").title()
    print(f"Hello {user_name}! I'm thinking of a number between 1 and 20.")
    ask_user=int(input("guess The Number\n"))
    number_of_tries=0
    while random_number !=ask_user:
        number_of_tries += 1
        if ask_user>random_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
        ask_user = int(input("guess The Number\n"))
    number_of_tries += 1
    print(f"Congratulations {user_name}, you guessed it in {number_of_tries} tries")
guessing_game()
