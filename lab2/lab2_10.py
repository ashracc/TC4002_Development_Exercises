# Course: TC4002 Analysis, Design and Construction of Software Systems
# Enrollment: A00354823
# Author: Juan Francisco Corral Stenner

"""
Create a class called myPowerList, implement methods for
- Adding items
- Removing the n-th item
"""

class myPowerList:
    """This class will only implement two methods"""
    def __init__(self, items):
        self.items = items

    def add_item(self, item_to_append):
        """Add an item to your items"""
        try:
            self.items.append(item_to_append)
        except:
            print(" Unable to append:", item_to_append)

    def remove_item(self, idx_of_item):
        """Remove an item from your items"""
        try:
            # self.items.remove(item_to_remove)
            del self.items[idx_of_item]
        except:
            print(" Unable to remove item at index:", idx_of_item)

def main():
    #    help(myPowerList)
    myPowerList1 = myPowerList([1, 3, 5, 4])

    print("Before adding:  ", myPowerList1.items)
    myPowerList1.add_item(10)
    print("After adding:   ", myPowerList1.items)

    print("Before removing:", myPowerList1.items)
    myPowerList1.remove_item(3)
    print("After removing: ", myPowerList1.items)


if __name__ == '__main__':
    main()