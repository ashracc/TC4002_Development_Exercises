# Course: TC4002 Analysis, Design and Construction of Software Systems
# Enrollment: A00354823
# Author: Juan Francisco Corral Stenner

"""
Add a method in myPowerList to return the sorted list
[ Do not use list.sort, implement the algorithm iterating in the list]
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

    def bubble_sort(self):
        flag = True
        while flag:
            flag = False
            for idx in range(len(self.items) - 1):
                if self.items[idx] > self.items[idx + 1]:
                    self.items[idx], self.items[idx + 1] = self.items[idx + 1], self.items[idx]
                    flag = True
        return self.items


def main():
    #    help(myPowerList)
    myPowerList1 = myPowerList([1, 7, 2, 27, 88, 3, 5, 4])

    print("Before sorting:", myPowerList1.items)
    myPowerList1.bubble_sort()
    print("After sorting: ", myPowerList1.items)

if __name__ == '__main__':
    main()