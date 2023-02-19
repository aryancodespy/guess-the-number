import random 

def playGame():

    randomNumber = random.randint(0, 10)
    guess_limit = 3
    number_of_guess = 0

    while number_of_guess != guess_limit :

        guess = int(input("Enter your guessed number: "))
        number_of_guess += 1

        if guess == randomNumber:
            print("Congratulations! You guessed the correct number.")

            play_again = input("Do you want to play again? y/n > ").lower()
            
            if play_again == "y":
                playGame()
            else:
                print("Thanks for playing.")
                exit()

        elif guess != randomNumber and number_of_guess != guess_limit:
            print("Sorry, Try Again!")

        else:
            print("Game Over!")

            play_again = input("Do you want to play again? y/n > ").lower()

            if play_again == "y":
                playGame()
            else:
                print("Thanks for playing.")
                exit()

playGame()