"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list
minus all the duplicates.
Write two different functions to do this - one using a loop and constructing a list, and another using sets.
[1,1,2,3,4,5,1,5,7,7,8,9,0,0,0,0]
[a,1,b,0,b,1,e,r,t,p,q]
[]
Add more test cases for large lists
"""

def delDupsUsingFor(myList):
    myList.sort()
    print(" Original list: {0}".format(myList))
    noDupList = []
    for item in myList:
        if item not in noDupList:
            noDupList.append(item)
    print(" Without dups:  {0}".format(noDupList))

def defDupsUsingSet(myList):
    print(" Original list: {0}".format(myList))
    noDupList = list(set(myList))
    print(" Without dups:  {0}".format(noDupList))

def main():
    ds1 = [1,1,2,3,4,5,1,5,7,7,8,9,0,0,0,0]
    ds2 = ['a','1','b','0','b','1','e','r','t','p','q' ]
    ds3 = []

    delDupsUsingFor(ds1)
    delDupsUsingFor(ds2)
    delDupsUsingFor(ds3)

    print("============")

    defDupsUsingSet(ds1)
    defDupsUsingSet(ds2)
    defDupsUsingSet(ds3)

if __name__ == '__main__':
    main()