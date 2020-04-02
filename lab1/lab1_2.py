"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether
they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first
exercise)
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
Record three runs
"""
import random

def main():
    count = 0
    myNum = random.randrange(1, 10)
    yourNum = ""
    while True:
        yourNum = input("What is your guess? \"exit\" to quit: ")
        if yourNum == "exit":
            print(" You tried", count, "without guessing, bye...")
            break
        count += 1
        if not yourNum.strip().isdigit():
            print(" Your guess must be a number between 1 and 9 inclusive.")
            continue
        if int(yourNum) > myNum:
            print("", yourNum, "is to high, try again.")
        elif int(yourNum) < myNum:
            print("", yourNum, "is to low, try again.")
        else:
            print(" You guess it! Number of tries:", count)
            break

if __name__ == "__main__":
    main()