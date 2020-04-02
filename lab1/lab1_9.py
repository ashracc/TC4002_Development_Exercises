# Write a function that converts a decimal number into a Roman format

so = "\u0305" # Single Overline
do = "\u033F" # Double Overline

romanSyms = {"I":      1,         "IV":                 4,         "V":      5,         "IX":                 9,
             "X":      10,        "XL":                 40,        "L":      50,        "XC":                 90,
             "C":      100,       "CD":                 400,       "D":      500,       "CM":                 900,
             "M":      1000,      "MV" + so:            4000,      "V" + so: 5000,      "MX" + so:            9000,
             "X" + so: 10000,     "X"  + so + "L" + so: 40000,     "L" + so: 50000,     "X"  + so + "C" + so: 90000,
             "C" + so: 100000,    "C"  + so + "D" + so: 400000,    "D" + so: 500000,    "C"  + so + "M" + so: 900000,
             "M" + so: 1000000,   "M"  + do + "V" + do: 4000000,   "V" + do: 5000000,   "M"  + do + "X" + do: 9000000,
             "X" + do: 10000000,  "X"  + do + "L" + do: 40000000,  "L" + do: 50000000,  "X"  + do + "C" + do: 90000000,
             "C" + do: 100000000, "C"  + do + "D" + do: 400000000, "D" + do: 500000000, "C"  + do + "M" + do: 900000000,
             "M" + do: 1000000000
             }

def decimal2roman(inputNum):
    flag = None
    for sym,num in romanSyms.items():
        if inputNum == num: return sym
        if inputNum > num:
            flag = sym
    remainder = inputNum - romanSyms[flag]
    return flag + decimal2roman(remainder)

#def printTest():
#    for key, value in romanSyms.items():
#        if value > 3999:
#            print("{0}: {1}".format(key, value))

def main():
    # printTest()
    yourNum = input("Provide a number: ")
    if not (yourNum.strip().isdigit()) or (int(yourNum) < 1) or (int(yourNum) > 3999999999):
        print("Not a valid input.")
    #elif (int(yourNum) < 1) or (int(yourNum) > 3999999999):
    #    print("Out of range")
    else:
        print("{0:>16}: {1:<16}".format("{0:,}".format(int(yourNum)), decimal2roman(int(yourNum))))

if __name__ == "__main__":
    main()