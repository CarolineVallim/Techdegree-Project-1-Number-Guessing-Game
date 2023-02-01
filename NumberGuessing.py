import random

high_score = []

def instructions():
    print("     NUMBER GUESSING GAME       ")
    print('-' * 30)
    print("""
        Instructions
        1. I got random number between 1 - 10
        2. For you win this game, you need to get the right number 
        3. You can try many times 
        4. If you get a incorrect number, I will help you with some directions
        """)
    print("Now, you know all the rules, we can star the game:)")
    print('-' * 30)

def type():
    try:
        attempt = int(input("Type a number:  "))
        if attempt < 1:
            print("This number need to be between 1-10. Try again")
            return type()
        elif attempt > 10 :
            print("This number need to be between 1-10. Try again")
            return type()
        return attempt
    except ValueError as err:
        print("This attempt need to be a number between 1-10. Try again")
        return type()

def start_game():
    instructions()
    right_number = random.randint(1,10)
    right_number = int(right_number)

    attempt = type()
    attempt_number = 1

    while attempt != right_number:
        attempt_number = attempt_number + 1
        if attempt > right_number:
            print("It's lower. Try again!")
            attempt = type()
        else:
            print("It's bigger. Try again!")
            attempt = type()
            

    print("""
You won!!! Congratulations!!!
    """)
    print("Your number of attempt was {}".format(attempt_number))
    high_score.append(attempt_number)

    proceed_game = input("""
Do you like to play again? y/n  """)  
    if proceed_game == "y":
        print("""
HIGH SCORE: The minimum number of the attempt was {}
        """.format(min(high_score)))
        start_game()
    else:
        print("Thank you for play the game")


start_game()
