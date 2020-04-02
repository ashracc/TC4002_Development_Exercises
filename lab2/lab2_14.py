# Course: TC4002 Analysis, Design and Construction of Software Systems
# Enrollment: A00354823
# Author: Juan Francisco Corral Stenner

"""
Add a method in myPowerList to read values for a List from a Text file
- readFromTextFile(filename)
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
        """Sort your items"""
        flag = True
        while flag:
            flag = False
            for idx in range(len(self.items) - 1):
                if self.items[idx] > self.items[idx + 1]:
                    self.items[idx], self.items[idx + 1] = self.items[idx + 1], self.items[idx]
                    flag = True
        return self.items

    def Lmerge(self,list_to_merge):
        """merge the list from left, as prefix"""
        self.items = list_to_merge + self.items
        return self.items

    def Rmerge(self,list_to_merge):
        """merge the list from right, as suffix"""
        self.items = self.items + list_to_merge
        return self.items

    def saveToTextFile(self, file_name):
        """Saves the content of your items to a file"""
        try:
            with open(file_name, 'w') as file_obj:
                for item in self.items:
                    print(item, file=file_obj)
            print(file_name, "successfully created")
        except:
            print(" Unable to write: ", file_name)

    def readFromTextFile(self, file_name):
        """Reads the content of your file"""
        try:
            with open(file_name, 'r') as file_obj:
                self.file_content = file_obj.read()
                print("The content of", file_name, "is:")
                print(self.file_content)
        except:
            print(" Unable to read: ", file_name)

def main():
    #    help(myPowerList)
    myPowerList1 = myPowerList([1, 7, 2, 27, 88, 3, 5, 4])
    file_name = "myPowerList.txt"
    myPowerList1.saveToTextFile(file_name)
    myPowerList1.readFromTextFile(file_name)

if __name__ == '__main__':
    main()