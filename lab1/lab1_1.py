"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides
evenly into num, tell that to the user. If not, print a different appropriate message.
"""

def isEven(num):
    extraMsg = ""
    if num % 2 == 0:
        if num % 4 == 0:
            extraMsg = "and multiple of 4"
        print(" {0} is an even number {1}".format(num,extraMsg))
    else:
        print(" {0} is an odd number".format(num))

def isDiv(num, check):
    if num % check == 0:
        print(" {0} can be evenly divided by {1}".format(num, check))
    else:
        print(" {0} cannot be evenly divided by {1}".format(num, check))

def main():
    number = num = check = ""
    while not number.strip().isdigit() or int(number.strip()) < 1:
        number = input("Provide a number: ")
        if not number.strip().isdigit() or int(number.strip()) < 1:
            print(" Not a valid number")
    isEven(int(number))

    while not num.strip().isdigit() or not check.strip().isdigit() or int(num.strip()) < 1 or int(check.strip()) < 1:
        num   = input("Provide \"num\": ")
        check = input("Provide \"check\": ")
        if not num.strip().isdigit() or not check.strip().isdigit() or int(num.strip()) < 1 or int(check.strip()) < 1:
            print(" \"num\" or/and \"check\" were not valid")
    isDiv(int(num), int(check))

if __name__ == "__main__":
    main()