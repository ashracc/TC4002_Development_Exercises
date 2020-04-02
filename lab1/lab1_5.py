"""
Write a function that receives as parameters how many Fibonnaci numbers to generate and then generates them. Take this
opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the
sequence to generate.(Hint: The Fibonnaci sequence is a sequence of numbers where the next number in the sequence is the
 sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

def fibonnaci(x):
    if x <= 1:
        return x
    else:
        return (fibonnaci(x - 1) + fibonnaci(x - 2))

def main():
    fibonacciList = []

    while True:
        numberOfFibos = input("How many fibonnaci numbers? ")
        if not numberOfFibos.strip().isdigit():
            print("Not a valid number")
        else:
            for x in range(int(numberOfFibos)):
                fibonacciList.append(fibonnaci(x))
            print(fibonacciList)
            break

if __name__ == '__main__':
    main()