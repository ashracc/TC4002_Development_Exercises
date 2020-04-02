"""
Write a function that evaluates if a given list satisfy Fibonacci sequence
returning true or false if the list satisfy the criteria
"""
def isFibonnaciSerie(fiboList):
    if len(fiboList) < 3:
        return False
    else:
        for idx in range(len(fiboList) - 2):
            if fiboList[idx] + fiboList[idx + 1] != fiboList[idx + 2]:
                return False
    return True

def main():
    ds1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229]
    ds2 = []
    ds3 = [0, 1, 1, 2, 3, 5, 8, 1, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]
    ds4 = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657]
    ds5 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657]
    ds6 = [75025, 121393, 196418, 317811, 514229]
    ds7 = [0]
    ds8 = [0, 2]
    ds9 = [0, 1]

    ds = [ds1, ds2, ds3, ds4, ds5, ds6, ds7, ds8, ds9]

    for ls in ds:
        if isFibonnaciSerie(ls):
            print(" Valid Fibonnaci serie:  ", ls)
        else:
            print(" Invalid Fibonnaci serie:", ls)

if __name__ == '__main__':
    main()