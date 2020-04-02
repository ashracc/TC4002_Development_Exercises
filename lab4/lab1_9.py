# Write a function that converts a decimal number into a Roman format

SO = "\u0305" # Single Overline
DO = "\u033F" # Double Overline

romanSyms = {"I":      1,         "IV":                 4,         "V":      5,         "IX":                 9,
             "X":      10,        "XL":                 40,        "L":      50,        "XC":                 90,
             "C":      100,       "CD":                 400,       "D":      500,       "CM":                 900,
             "M":      1000,      "MV" + SO:            4000,      "V" + SO: 5000,      "MX" + SO:            9000,
             "X" + SO: 10000,     "X"  + SO + "L" + SO: 40000,     "L" + SO: 50000,     "X"  + SO + "C" + SO: 90000,
             "C" + SO: 100000,    "C"  + SO + "D" + SO: 400000,    "D" + SO: 500000,    "C"  + SO + "M" + SO: 900000,
             "M" + SO: 1000000,   "M"  + DO + "V" + DO: 4000000,   "V" + DO: 5000000,   "M"  + DO + "X" + DO: 9000000,
             "X" + DO: 10000000,  "X"  + DO + "L" + DO: 40000000,  "L" + DO: 50000000,  "X"  + DO + "C" + DO: 90000000,
             "C" + DO: 100000000, "C"  + DO + "D" + DO: 400000000, "D" + DO: 500000000, "C"  + DO + "M" + DO: 900000000,
             "M" + DO: 1000000000
             }

def decimal2roman(inputNum):
    if type(inputNum) not in [int]:
        raise TypeError("The input must be a non-negative number.")
    if inputNum < 1 or inputNum > 3999999999:
        raise ValueError("The input must be between 1 and 3999999999 inclusive.")
    flag = None
    for sym,num in romanSyms.items():
        if inputNum == num:
            return sym
        if inputNum > num:
            flag = sym
    remainder = inputNum - romanSyms[flag]
    return flag + decimal2roman(remainder)