# Course: TC4002 Analysis, Design and Construction of Software Systems
# Enrollment: A00354823
# Author: Juan Francisco Corral Stenner

"""
Implement a class that manages a directory that is saved in a text file. The data saved includes:
a. Name
b. Email
c. Age
d. Country of Origin
The class should have capabilities to:
- Add new record
- Delete a record
- Look for a record by mail and age
- List on screen all records
"""

class Person:
    name = []

    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1

    def get_name(self, user_id):
        if user_id >= len(self.name):
            return 'There is no such user'
        else:
            return self.name[user_id]

if __name__ == '__main__':
    person = Person()
    print('User Abbas has been added with id ', person.set_name('Abbas'))
    print('User associated with id 0 is ', person.get_name(0))